@echo off
:: requires Administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb runAs -Wait"
    exit /b
)
:: bat
cd /d %~dp0

:: Run Program main

wsl --shutdown
wsl --list --verbose
dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart
dism.exe /online /disable-feature /featurename:VirtualMachinePlatform /norestart
dism.exe /online /disable-feature /featurename:Microsoft-Hyper-V-All /norestart

if %errorlevel% neq 0 (
    echo Failed to execute the program.
    pause
)
pause
