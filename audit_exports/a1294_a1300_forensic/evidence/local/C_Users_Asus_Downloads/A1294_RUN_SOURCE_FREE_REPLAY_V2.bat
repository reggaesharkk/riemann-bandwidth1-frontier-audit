@echo off
setlocal EnableExtensions
title A1294 Source-Free Replay V2 Launcher
set "DL=%USERPROFILE%\Downloads"
set "WORK=%DL%\A1294_SOURCE_FREE_REPLAY_V2"
set "PACKAGE=%DL%\A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip"

if not exist "%PACKAGE%" goto NOZIP
if exist "%WORK%" rmdir /s /q "%WORK%"
mkdir "%WORK%"

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '%PACKAGE%' -DestinationPath '%WORK%' -Force"
if errorlevel 1 goto FAIL

set "RUNNER=%WORK%\A1294_SOURCE_FREE_REPLAY_PACKAGE_V2\RUN_A1294_SOURCE_FREE_REPLAY.bat"
if not exist "%RUNNER%" goto FAIL

call "%RUNNER%"
exit /b %ERRORLEVEL%

:NOZIP
echo ERROR: Put A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip in Downloads.
pause
exit /b 1

:FAIL
echo ERROR: Could not extract or launch V2 package.
pause
exit /b 1
