@echo off
setlocal EnableExtensions
title A1296 Frontier Microscope
set "DL=%USERPROFILE%\Downloads"
set "BASE=%DL%\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE"
set "HERE=%~dp0"
set "LOG=%DL%\A1296_frontier_microscope_log.txt"

echo A1296 frontier microscope started > "%LOG%"
echo ============================================================
echo A1296 FRONTIER MICROSCOPE
echo ============================================================
echo.
echo This is a fast structural audit of the deepest 200 unresolved
echo boxes from the 5M A1296 run. It identifies the exact catalog
echo pieces and seam partial sums dominating the hard frontier.
echo.

if not exist "%BASE%\results\A1296_FULLROOT_5M_DIAGNOSTIC_RESULT.json" goto NORESULT

set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3"
if not defined PY_CMD (
  where python >nul 2>nul
  if %errorlevel%==0 set "PY_CMD=python"
)
if not defined PY_CMD goto NOPY

%PY_CMD% "%HERE%a1296_frontier_microscope.py" "%BASE%" >> "%LOG%" 2>&1
set "RC=%ERRORLEVEL%"
type "%LOG%"
echo.
if not "%RC%"=="0" goto FAIL

echo ============================================================
echo SUCCESS
echo ============================================================
echo Result:
echo %BASE%\results\A1296_FRONTIER_MICROSCOPE_RESULT.json
echo.
pause
exit /b 0

:NORESULT
echo ERROR: A1296 result JSON is missing from:
echo %BASE%\results
pause
exit /b 1

:NOPY
echo ERROR: Python 3 not found.
pause
exit /b 1

:FAIL
echo ERROR: Microscope failed. Send:
echo %LOG%
pause
exit /b %RC%
