@echo off
setlocal EnableExtensions
title A1294 Full-Root Bracket Launcher
set "DL=%USERPROFILE%\Downloads"
set "WORK=%DL%\A1294_FULLROOT_BRACKET"
set "PACKAGE="

for %%F in ("%DL%\A1294_FULLROOT_BRACKET_PACKAGE*.zip") do if exist "%%~fF" set "PACKAGE=%%~fF"
if not defined PACKAGE goto NOZIP

if exist "%WORK%" rmdir /s /q "%WORK%"
mkdir "%WORK%"
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '%PACKAGE%' -DestinationPath '%WORK%' -Force"
if errorlevel 1 goto FAIL

set "RUNNER=%WORK%\A1294_FULLROOT_BRACKET_PACKAGE\RUN_FULLROOT_1M_BRACKET.bat"
if not exist "%RUNNER%" goto FAIL
call "%RUNNER%"
exit /b %ERRORLEVEL%

:NOZIP
echo ERROR: Put A1294_FULLROOT_BRACKET_PACKAGE.zip in Downloads.
pause
exit /b 1

:FAIL
echo ERROR: Could not extract/start package.
pause
exit /b 1
