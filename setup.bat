@echo off
:: requires Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Program requires Administrator privileges Restarting...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

:: bat
cd /d %~dp0

:: Run Program main
python "commanding\setup.py"
python.exe -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo [ERROR] Failed to execute the program.
    pause
)