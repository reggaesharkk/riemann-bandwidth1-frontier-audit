@echo off
setlocal
title A1294 Benchmark - START HERE

set "DL=%USERPROFILE%\Downloads"
set "LOG=%DL%\A1294_launcher_log.txt"
set "WORK=%DL%\A1294_LOCAL_BENCHMARK"
set "PACKAGE="

echo A1294 launcher started > "%LOG%"
echo Downloads: %DL% >> "%LOG%"
echo.

echo ============================================================
echo A1294 LOCAL BENCHMARK - START HERE
echo ============================================================
echo Downloads folder:
echo   %DL%
echo.

for %%F in ("%DL%\A1294_LOCAL_BENCHMARK_PACKAGE*.zip") do if exist "%%~fF" set "PACKAGE=%%~fF"

if not defined PACKAGE goto NOZIP

echo Found ZIP:
echo   %PACKAGE%
echo Found ZIP: %PACKAGE% >> "%LOG%"
echo.

if exist "%WORK%" (
  echo Removing old extracted folder...
  rmdir /s /q "%WORK%" >> "%LOG%" 2>&1
)

mkdir "%WORK%" >> "%LOG%" 2>&1

echo Extracting...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '%PACKAGE%' -DestinationPath '%WORK%' -Force" >> "%LOG%" 2>&1

if errorlevel 1 goto EXTRACTFAIL

set "RUNNER=%WORK%\A1294_LOCAL_BENCHMARK_PACKAGE\RUN_BENCHMARK.bat"

if not exist "%RUNNER%" goto NORUNNER

echo Extraction complete.
echo Starting benchmark now...
echo.
echo Runner: %RUNNER% >> "%LOG%"

call "%RUNNER%"
set "RC=%ERRORLEVEL%"

echo.
echo Benchmark exit code: %RC%
echo Benchmark exit code: %RC% >> "%LOG%"

if not "%RC%"=="0" goto BENCHFAIL

echo.
echo ============================================================
echo SUCCESS
echo ============================================================
echo.
echo Send this file back to ChatGPT:
echo.
echo %WORK%\A1294_LOCAL_BENCHMARK_PACKAGE\results\A1294_LOCAL_BENCHMARK_RESULT.json
echo.
echo Log file:
echo %LOG%
echo.
pause
exit /b 0

:NOZIP
echo ERROR: Benchmark ZIP was not found in Downloads.
echo ERROR NOZIP >> "%LOG%"
echo.
echo The ZIP filename must start with:
echo A1294_LOCAL_BENCHMARK_PACKAGE
echo.
echo Put the ZIP in:
echo %DL%
echo.
echo This window will stay open.
pause
exit /b 1

:EXTRACTFAIL
echo.
echo ERROR: ZIP extraction failed.
echo ERROR EXTRACTFAIL >> "%LOG%"
echo.
echo Open this log file and send it to ChatGPT:
echo %LOG%
echo.
pause
exit /b 1

:NORUNNER
echo.
echo ERROR: RUN_BENCHMARK.bat was not found after extraction.
echo ERROR NORUNNER >> "%LOG%"
echo.
echo Send this log file to ChatGPT:
echo %LOG%
echo.
pause
exit /b 1

:BENCHFAIL
echo.
echo ERROR: Benchmark failed.
echo ERROR BENCHFAIL >> "%LOG%"
echo.
echo Send this log file to ChatGPT:
echo %LOG%
echo.
pause
exit /b %RC%
