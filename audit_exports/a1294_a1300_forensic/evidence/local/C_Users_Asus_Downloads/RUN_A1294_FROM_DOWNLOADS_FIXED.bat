@echo off
setlocal EnableExtensions
title A1294 Local Benchmark Launcher - FIXED

echo ============================================================
echo A1294 LOCAL BENCHMARK LAUNCHER - FIXED
echo ============================================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"$ErrorActionPreference='Stop';" ^
"$downloads = Join-Path $env:USERPROFILE 'Downloads';" ^
"Write-Host ('Downloads folder: ' + $downloads);" ^
"$zip = Get-ChildItem -LiteralPath $downloads -Filter 'A1294_LOCAL_BENCHMARK_PACKAGE*.zip' -File | Sort-Object LastWriteTime -Descending | Select-Object -First 1;" ^
"if(-not $zip){ throw 'Could not find A1294_LOCAL_BENCHMARK_PACKAGE*.zip in Downloads.' };" ^
"Write-Host ('Found package: ' + $zip.FullName);" ^
"$work = Join-Path $downloads 'A1294_LOCAL_BENCHMARK';" ^
"if(Test-Path -LiteralPath $work){ Remove-Item -LiteralPath $work -Recurse -Force };" ^
"New-Item -ItemType Directory -Path $work | Out-Null;" ^
"Write-Host ('Extracting to: ' + $work);" ^
"Expand-Archive -LiteralPath $zip.FullName -DestinationPath $work -Force;" ^
"$runner = Join-Path $work 'A1294_LOCAL_BENCHMARK_PACKAGE\RUN_BENCHMARK.bat';" ^
"if(-not (Test-Path -LiteralPath $runner)){ throw ('RUN_BENCHMARK.bat not found at ' + $runner) };" ^
"Write-Host '';" ^
"Write-Host 'Starting benchmark...';" ^
"& cmd.exe /c ('\"' + $runner + '\"');" ^
"$code = $LASTEXITCODE;" ^
"if($code -ne 0){ throw ('Benchmark exited with code ' + $code) };" ^
"Write-Host '';" ^
"Write-Host 'Benchmark completed successfully.';" ^
"Write-Host ('Result file: ' + (Join-Path $work 'A1294_LOCAL_BENCHMARK_PACKAGE\results\A1294_LOCAL_BENCHMARK_RESULT.json'));"

set "RC=%errorlevel%"
echo.
if not "%RC%"=="0" (
  echo ============================================================
  echo FAILED
  echo ============================================================
  echo Send me a screenshot of this window.
  echo.
  pause
  exit /b %RC%
)

echo ============================================================
echo SUCCESS
echo ============================================================
echo Send this file back to ChatGPT:
echo %USERPROFILE%\Downloads\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE\results\A1294_LOCAL_BENCHMARK_RESULT.json
echo.
pause
