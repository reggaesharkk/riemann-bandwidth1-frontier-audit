@echo off
setlocal EnableExtensions
title A1296 Full-Root 5M Diagnostic
set "DL=%USERPROFILE%\Downloads"
set "BASE=%DL%\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE"
set "HERE=%~dp0"
set "LOG=%DL%\A1296_5m_diagnostic_log.txt"

echo A1296 5M diagnostic started > "%LOG%"
echo ============================================================
echo A1296 FULL-ROOT 5M DIAGNOSTIC
echo ============================================================
echo A = 0.012960
echo B = 1094977/5000000000
echo.
echo This is the strongest sensible current-catalog target below
echo the exact frozen-catalog ceiling witness ~0.0129615832.
echo.
echo Six workers, 5,000,000-node budget.
echo Expected runtime: roughly 25-45 minutes.
echo.

if not exist "%BASE%\a1294_seam_pilot.py" goto NOBASE
set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3"
if not defined PY_CMD (
  where python >nul 2>nul
  if %errorlevel%==0 set "PY_CMD=python"
)
if not defined PY_CMD goto NOPY

%PY_CMD% "%HERE%a1296_5m.py" --base "%BASE%" --workers 6 --chunk-nodes 10000 --budget 5000000 --initial-boxes 32 >> "%LOG%" 2>&1
set "RC=%ERRORLEVEL%"
type "%LOG%"
echo.
if not "%RC%"=="0" goto FAIL
echo ============================================================
echo SUCCESS
echo ============================================================
echo Result:
echo %BASE%\results\A1296_FULLROOT_5M_DIAGNOSTIC_RESULT.json
echo.
pause
exit /b 0

:NOBASE
echo ERROR: Existing benchmark folder missing.
pause
exit /b 1
:NOPY
echo ERROR: Python 3 not found.
pause
exit /b 1
:FAIL
echo ERROR: Diagnostic failed. Send:
echo %LOG%
pause
exit /b %RC%
