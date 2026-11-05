@echo off
setlocal EnableExtensions EnableDelayedExpansion
title A1294 Local Benchmark Launcher

set "DOWNLOADS=%USERPROFILE%\Downloads"

if not exist "%DOWNLOADS%" (
  for /f "usebackq delims=" %%D in (`powershell -NoProfile -Command "$k='{374DE290-123F-4565-9164-39C4925E467B}'; $p=(Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders').$k; [Console]::Write([Environment]::ExpandEnvironmentVariables($p))"`) do set "DOWNLOADS=%%D"
)

echo ============================================================
echo A1294 LOCAL BENCHMARK LAUNCHER
echo ============================================================
echo Downloads folder:
echo   %DOWNLOADS%
echo.

if not exist "%DOWNLOADS%" (
  echo ERROR: Could not find your Downloads folder.
  pause
  exit /b 1
)

set "PACKAGE="
for /f "usebackq delims=" %%F in (`powershell -NoProfile -Command "$f=Get-ChildItem -LiteralPath '%DOWNLOADS%' -Filter 'A1294_LOCAL_BENCHMARK_PACKAGE*.zip' -File ^| Sort-Object LastWriteTime -Descending ^| Select-Object -First 1; if($f){[Console]::Write($f.FullName)}"`) do set "PACKAGE=%%F"

if not defined PACKAGE (
  echo ERROR: I could not find:
  echo   A1294_LOCAL_BENCHMARK_PACKAGE*.zip
  echo in:
  echo   %DOWNLOADS%
  echo.
  echo Download the ZIP into Downloads and run this BAT again.
  pause
  exit /b 1
)

echo Found package:
echo   %PACKAGE%
echo.

set "WORK=%DOWNLOADS%\A1294_LOCAL_BENCHMARK"

echo Extracting to:
echo   %WORK%
echo.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$ErrorActionPreference='Stop';" ^
  "if(Test-Path -LiteralPath '%WORK%'){Remove-Item -LiteralPath '%WORK%' -Recurse -Force};" ^
  "New-Item -ItemType Directory -Path '%WORK%' | Out-Null;" ^
  "Expand-Archive -LiteralPath '%PACKAGE%' -DestinationPath '%WORK%' -Force"

if errorlevel 1 (
  echo ERROR: Extraction failed.
  pause
  exit /b 1
)

set "RUNNER=%WORK%\A1294_LOCAL_BENCHMARK_PACKAGE\RUN_BENCHMARK.bat"

if not exist "%RUNNER%" (
  echo ERROR: RUN_BENCHMARK.bat was not found after extraction.
  pause
  exit /b 1
)

echo Starting benchmark...
echo.
call "%RUNNER%"
exit /b %errorlevel%
