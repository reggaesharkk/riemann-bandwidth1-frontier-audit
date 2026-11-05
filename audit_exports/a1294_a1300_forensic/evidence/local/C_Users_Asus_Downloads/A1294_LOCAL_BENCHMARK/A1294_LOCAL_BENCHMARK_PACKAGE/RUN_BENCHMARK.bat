@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo A1294 LOCAL BENCHMARK - Snapdragon / Windows
echo ============================================================
echo.

set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3"

if not defined PY_CMD (
  where python >nul 2>nul
  if %errorlevel%==0 set "PY_CMD=python"
)

if not defined PY_CMD (
  echo ERROR: Python 3 was not found.
  echo.
  echo Install Python 3 for Windows ARM64, then run this file again.
  echo In VS Code you can also select your Python interpreter and rerun.
  echo.
  pause
  exit /b 1
)

echo Using: %PY_CMD%
echo.
%PY_CMD% benchmark_local.py --single-nodes 250000 --parallel-nodes-per-box 40000 --workers 6 --subboxes 8
set "RC=%errorlevel%"

echo.
if not "%RC%"=="0" (
  echo Benchmark failed with exit code %RC%.
  echo Send a screenshot of this window to ChatGPT.
  pause
  exit /b %RC%
)

echo Benchmark finished.
echo Send this file to ChatGPT:
echo   %~dp0results\A1294_LOCAL_BENCHMARK_RESULT.json
echo.
pause
