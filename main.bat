@echo off
py "%~dp0main.py"

if errorlevel 1 (
    echo.
    echo The program exited with an error.
    pause
)