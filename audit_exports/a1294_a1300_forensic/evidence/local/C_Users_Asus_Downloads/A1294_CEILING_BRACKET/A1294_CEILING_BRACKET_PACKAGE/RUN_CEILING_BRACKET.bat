@echo off
setlocal EnableExtensions
title A1294 Fixed-B Ceiling Bracket

set "DL=%USERPROFILE%\Downloads"
set "BASE=%DL%\A1294_LOCAL_BENCHMARK\A1294_LOCAL_BENCHMARK_PACKAGE"
set "HERE=%~dp0"
set "LOG=%DL%\A1294_ceiling_bracket_log.txt"

echo A1294 fixed-B ceiling bracket started > "%LOG%"
echo Base: %BASE% >> "%LOG%"

echo ============================================================
echo A1294 FIXED-B CEILING BRACKET
echo ============================================================
echo.
echo Testing hard A1299 boxes at:
echo 0.012990  0.012992  0.012994  0.012996  0.012998  0.013000
echo.
echo This is diagnostic, not a theorem.
echo.

if not exist "%BASE%\results\A1294_A1299_ADAPTIVE_FRONTIER_RESULT.json" goto NOPREV

set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3"
if not defined PY_CMD (
  where python >nul 2>nul
  if %errorlevel%==0 set "PY_CMD=python"
)
if not defined PY_CMD goto NOPY

echo Starting 6-worker targeted exact scan...
echo Expected runtime: about 10-20 minutes.
echo.

%PY_CMD% "%HERE%ceiling_bracket.py" ^
  --base "%BASE%" ^
  --workers 6 ^
  --chunk-nodes 5000 ^
  --budget 180000 ^
  >> "%LOG%" 2>&1

set "RC=%ERRORLEVEL%"
type "%LOG%"
echo.

if not "%RC%"=="0" goto FAIL

echo ============================================================
echo SUCCESS
echo ============================================================
echo Result:
echo %BASE%\results\A1294_FIXED_B_CEILING_BRACKET_RESULT.json
echo.
pause
exit /b 0

:NOPREV
echo ERROR: Previous adaptive result JSON not found.
echo Sync/copy A1294_A1299_ADAPTIVE_FRONTIER_RESULT.json into:
echo %BASE%\results
echo.
pause
exit /b 1

:NOPY
echo ERROR: Python 3 not found.
pause
exit /b 1

:FAIL
echo ERROR: Ceiling bracket failed.
echo Send:
echo %LOG%
pause
exit /b %RC%
