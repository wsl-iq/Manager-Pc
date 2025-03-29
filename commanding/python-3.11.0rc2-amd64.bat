@echo off
setlocal

:: Move to script directory
cd /d %~dp0

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel%==0 (
    echo Python is already installed. Continuing execution...
    goto :continue
) else (
    echo Python is not installed. Installing now...
)

:: Install Python for the current user only (no admin needed)
"python-3.11.0rc2-amd64.exe" /quiet PrependPath=1

:: Wait and verify installation
echo Verifying installation...
timeout /t 10 >nul

:: Check again if Python is installed
where python >nul 2>nul
if %errorlevel%==0 (
    echo Python has been successfully installed.
) else (
    echo Installation failed! Ensure the installer file is present.
    exit /b 1
)

:continue
echo Continuing execution...
:: Add any other commands here after ensuring Python is installed
