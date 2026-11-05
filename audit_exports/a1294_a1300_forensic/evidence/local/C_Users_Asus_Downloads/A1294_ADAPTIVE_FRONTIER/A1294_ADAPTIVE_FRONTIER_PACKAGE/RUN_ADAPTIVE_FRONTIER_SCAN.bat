@echo off
setlocal EnableExtensions
title A1294-A1299 Adaptive Frontier Scan

set "DL=%USERPROFILE%\Downloads"
set "BASE=%DL%\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE"
set "HERE=%~dp0"
set "LOG=%DL%\A1294_adaptive_scan_log.txt"

echo A1294-A1299 adaptive scan started > "%LOG%"
echo Base: %BASE% >> "%LOG%"

echo ============================================================
echo A1294-A1299 ADAPTIVE FRONTIER SCAN
echo ============================================================
echo.
echo Existing benchmark folder:
echo   %BASE%
echo.

if not exist "%BASE%\a1294_seam_pilot.py" goto NOBASE
if not exist "%BASE%\data\macro-data-exact.json" goto NOBASE

set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3"
if not defined PY_CMD (
  where python >nul 2>nul
  if %errorlevel%==0 set "PY_CMD=python"
)
if not defined PY_CMD goto NOPY

echo Using: %PY_CMD%
echo.
echo This scans A1294 through A1299 with exact arithmetic.
echo It is diagnostic only; it does NOT claim a theorem.
echo.
echo Expected runtime: roughly 10-25 minutes on your laptop.
echo.
echo Starting...
echo.

%PY_CMD% "%HERE%adaptive_frontier_scan.py" ^
  --base "%BASE%" ^
  --workers 6 ^
  --chunk-nodes 5000 ^
  --initial-boxes 32 ^
  --budget-per-candidate 80000 ^
  >> "%LOG%" 2>&1

set "RC=%ERRORLEVEL%"

type "%LOG%"
echo.

if not "%RC%"=="0" goto FAILED

echo ============================================================
echo SUCCESS
echo ============================================================
echo.
echo Result file:
echo %BASE%\results\A1294_A1299_ADAPTIVE_FRONTIER_RESULT.json
echo.
echo If your benchmark folder syncs to Drive, I can read it there.
echo Otherwise upload that JSON.
echo.
pause
exit /b 0

:NOBASE
echo ERROR: Existing A1294 benchmark folder was not found.
echo Expected:
echo %BASE%
echo.
pause
exit /b 1

:NOPY
echo ERROR: Python 3 not found.
echo.
pause
exit /b 1

:FAILED
echo ============================================================
echo FAILED
echo ============================================================
echo Send me:
echo %LOG%
echo.
pause
exit /b %RC%
