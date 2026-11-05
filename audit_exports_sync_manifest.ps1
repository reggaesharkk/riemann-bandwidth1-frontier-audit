$ErrorActionPreference = 'Stop'
$rootPath = (Resolve-Path 'audit_exports').Path
$repoRoot = (Resolve-Path '.').Path
$sourceExt = [System.Collections.Generic.HashSet[string]]::new([string[]]@('.lean','.py','.md','.json','.log','.txt','.csv','.sh','.bat','.yml','.toml','.tex','.cpp','.sha256','.sha256sums','.zlib','.sb01','.gitattributes','.template'), [System.StringComparer]::OrdinalIgnoreCase)
$all = @(Get-ChildItem -LiteralPath $rootPath -Recurse -File | Sort-Object FullName)
$sha = [System.Security.Cryptography.SHA256]::Create()
$records = [System.Collections.Generic.List[object]]::new()
$index = 0
foreach ($f in $all) {
  $relative = $f.FullName.Substring($rootPath.Length + 1).Replace([char]92, [char]47)
  $lower = $relative.ToLowerInvariant()
  $ext = $f.Extension.ToLowerInvariant()
  $isScratch = $lower.StartsWith('sharkbridge01_worktree/') -or $lower.Contains('/sharkbridge01_worktree/') -or $lower.StartsWith('__pycache__/') -or $lower.Contains('/__pycache__/')
  if ($isScratch) { $class = 'scratch_copy_excluded' }
  elseif ($sourceExt.Contains($ext) -and $f.Length -lt 104857600) { $class = 'git_source_and_evidence' }
  elseif ($ext -eq '.zip' -and $f.Length -lt 2147483648) { $class = 'github_release_candidate' }
  else { $class = 'local_binary_or_generated_artifact' }
  $stream = $null
  $hashStatus = if ($isScratch) { 'NOT_HASHED_SCRATCH' } else { 'OK' }
  if ($isScratch) { $digest = $null }
  else {
    try {
      $stream = [System.IO.File]::OpenRead($f.FullName)
      $digest = ([BitConverter]::ToString($sha.ComputeHash($stream))).Replace('-', '').ToLowerInvariant()
    }
    catch {
      $digest = $null
      $hashStatus = 'UNREADABLE: ' + $_.Exception.Message
      Write-Output ('hash failed ' + $relative + ' :: ' + $_.Exception.Message)
    }
    finally { if ($null -ne $stream) { $stream.Dispose() } }
  }
  $records.Add([pscustomobject]@{path=('audit_exports/' + $relative); size_bytes=[int64]$f.Length; sha256=$digest; hash_status=$hashStatus; sync_class=$class})
  $index++
  if (($index % 1000) -eq 0) { Write-Output "hashed $index / $($all.Count)" }
}
$summary = @($records | Group-Object sync_class | Sort-Object Name | ForEach-Object { [pscustomobject]@{sync_class=$_.Name; count=$_.Count; bytes=[int64](($_.Group | Measure-Object size_bytes -Sum).Sum)} })
$manifest = [pscustomobject]@{schema='riemann-audit-export-sync/v1'; generated_utc=[DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ'); source_root='audit_exports/'; source_commit=(git rev-parse HEAD).Trim(); file_count=$records.Count; summary=$summary; files=$records}
$manifestPath = Join-Path $repoRoot 'AUDIT_EXPORTS_SYNC_MANIFEST_20261106.json'
[System.IO.File]::WriteAllText($manifestPath, ($manifest | ConvertTo-Json -Depth 6), [System.Text.UTF8Encoding]::new($false))
$zipUnique = @($records | Where-Object {$_.sync_class -eq 'github_release_candidate' -and $null -ne $_.sha256} | Group-Object sha256 | ForEach-Object { $_.Group | Select-Object -First 1 })
$releasePath = Join-Path $repoRoot 'AUDIT_EXPORTS_RELEASE_ASSET_CANDIDATES_20261106.json'
[System.IO.File]::WriteAllText($releasePath, (@{unique_archive_count=$zipUnique.Count; unique_archive_bytes=[int64](($zipUnique|Measure-Object size_bytes -Sum).Sum); archives=$zipUnique} | ConvertTo-Json -Depth 5), [System.Text.UTF8Encoding]::new($false))
$sourcePaths = @($records | Where-Object {$_.sync_class -eq 'git_source_and_evidence' -and $null -ne $_.sha256} | ForEach-Object {$_.path})
$pathspecPath = Join-Path $repoRoot 'audit_exports_sync_paths.tmp'
[System.IO.File]::WriteAllText($pathspecPath, ($sourcePaths -join [char]0), [System.Text.UTF8Encoding]::new($false))
[pscustomobject]@{manifest=$manifestPath; file_count=$records.Count; class_summary=$summary; release_candidate_unique_count=$zipUnique.Count; release_candidate_unique_bytes=[int64](($zipUnique|Measure-Object size_bytes -Sum).Sum); source_path_count=$sourcePaths.Count; source_pathspec=$pathspecPath} | ConvertTo-Json -Depth 5 -Compress
