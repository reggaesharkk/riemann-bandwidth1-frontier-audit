@echo off
setlocal EnableExtensions
title A1294 Full-Root 1M Bracket

set "DL=%USERPROFILE%\Downloads"
set "BASE=%DL%\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE"
set "HERE=%~dp0"
set "LOG=%DL%\A1294_fullroot_1m_bracket_log.txt"

echo Full-root 1M bracket started > "%LOG%"
echo Base: %BASE% >> "%LOG%"

echo ============================================================
echo FULL-ROOT 1M BRACKET
echo ============================================================
echo.
echo Candidates:
echo   A1299  = 0.012990
echo   A12994 = 0.012994
echo   A1300  = 0.013000
echo.
echo Six workers, one million node diagnostic budget per candidate.
echo This is not a theorem unless a candidate fully closes.
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

echo Starting...
echo Expected runtime: roughly 15-30 minutes.
echo.

%PY_CMD% "%HERE%fullroot_bracket.py" ^
  --base "%BASE%" ^
  --workers 6 ^
  --chunk-nodes 10000 ^
  --budget 1000000 ^
  --initial-boxes 32 ^
  >> "%LOG%" 2>&1

set "RC=%ERRORLEVEL%"
type "%LOG%"
echo.

if not "%RC%"=="0" goto FAIL

echo ============================================================
echo SUCCESS
echo ============================================================
echo Result:
echo %BASE%\results\A1294_FULLROOT_1M_BRACKET_RESULT.json
echo.
pause
exit /b 0

:NOBASE
echo ERROR: Existing benchmark folder missing:
echo %BASE%
pause
exit /b 1

:NOPY
echo ERROR: Python 3 not found.
pause
exit /b 1

:FAIL
echo ERROR: Full-root bracket failed.
echo Send:
echo %LOG%
pause
exit /b %RC%
