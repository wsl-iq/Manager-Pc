@echo off
:: ============================================
:: Privacy Policy
:: Last updated: May 3, 2025
::
:: This script does NOT collect, store, or share any personal information.
:: It runs a Python file (main.py) and requires Administrator privileges 
:: only to ensure proper functionality.
::
:: No personal data is collected.
:: No internet communication is made.
:: No user or device information is stored.
::
:: Administrator privileges are used solely for technical execution purposes.
:: The script does not contain any malicious instructions or hidden operations.
:: You are free to inspect the code.
:: ============================================

:: Check for Administrator privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Program requires Administrator privileges. Restarting...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

:: Change to script directory
cd /d %~dp0

:: Run main Python program
python "main.py"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to execute the program.
    pause
)
