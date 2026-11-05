@echo off
setlocal EnableExtensions
title A1294 Adaptive Frontier Launcher

set "DL=%USERPROFILE%\Downloads"
set "WORK=%DL%\A1294_ADAPTIVE_FRONTIER"
set "PACKAGE="

echo ============================================================
echo A1294 ADAPTIVE FRONTIER LAUNCHER
echo ============================================================
echo.

for %%F in ("%DL%\A1294_ADAPTIVE_FRONTIER_PACKAGE*.zip") do if exist "%%~fF" set "PACKAGE=%%~fF"

if not defined PACKAGE goto NOZIP

echo Found:
echo   %PACKAGE%
echo.

if exist "%WORK%" rmdir /s /q "%WORK%"
mkdir "%WORK%"

echo Extracting...
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '%PACKAGE%' -DestinationPath '%WORK%' -Force"
if errorlevel 1 goto FAIL

set "RUNNER=%WORK%\A1294_ADAPTIVE_FRONTIER_PACKAGE\RUN_ADAPTIVE_FRONTIER_SCAN.bat"
if not exist "%RUNNER%" goto FAIL

call "%RUNNER%"
exit /b %ERRORLEVEL%

:NOZIP
echo ERROR: Put A1294_ADAPTIVE_FRONTIER_PACKAGE.zip in Downloads.
echo.
pause
exit /b 1

:FAIL
echo ERROR: Could not extract or start adaptive scan.
echo.
pause
exit /b 1
