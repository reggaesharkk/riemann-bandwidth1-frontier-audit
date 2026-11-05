@echo off
setlocal EnableExtensions
title A1294 Replay Preflight V2
cd /d "%~dp0"
set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py -3"
if not defined PY_CMD set "PY_CMD=python"
%PY_CMD% preflight.py
echo.
pause
