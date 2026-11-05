@echo off
setlocal EnableExtensions
title A1294 Source-Free Exact Replay
cd /d "%~dp0"
set "LOG=%~dp0A1294_SOURCE_FREE_REPLAY_LOG.txt"

echo ============================================================
echo A1294 SOURCE-FREE EXACT REPLAY
echo ============================================================
echo.
echo This replays all 13,454,121 certificate nodes with exact
echo Fraction arithmetic. It imports no generator or project code.
echo.
echo Expected runtime on the Snapdragon ARM64 laptop:
echo roughly 2-5 hours. Do not close this window.
echo.

set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3"
if not defined PY_CMD (
  where python >nul 2>nul
  if %errorlevel%==0 set "PY_CMD=python"
)
if not defined PY_CMD goto NOPY

echo A1294 source-free replay started > "%LOG%"
%PY_CMD% replay_a1294_source_free.py --package-root "%~dp0" --progress 250000 >> "%LOG%" 2>&1
set "RC=%ERRORLEVEL%"
type "%LOG%"
echo.

if not "%RC%"=="0" goto FAIL

echo ============================================================
echo PASS
echo ============================================================
echo Upload these two files to ChatGPT:
echo   A1294_SOURCE_FREE_REPLAY_RESULT.json
echo   A1294_SOURCE_FREE_REPLAY_LOG.txt
echo.
pause
exit /b 0

:NOPY
echo ERROR: Python 3 was not found.
pause
exit /b 1

:FAIL
echo ============================================================
echo REPLAY FAILED
echo ============================================================
echo Send A1294_SOURCE_FREE_REPLAY_LOG.txt to ChatGPT.
pause
exit /b %RC%
