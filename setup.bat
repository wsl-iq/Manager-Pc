@echo off
:: Move to script directory
cd /d %~dp0

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] Python is not installed. Installing now...
    
    :: Install Python for current user only (no admin needed)
    "commandng\python-3.11.0rc2-amd64.bat" /quiet PrependPath=1
    
    timeout /t 10 >nul
)

:: Verify Python installation
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python installation failed! Please check the installer file.
    exit /b 1
)

:: Upgrade pip and run the setup script
python.exe -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo [ERROR] Failed to upgrade pip.
    exit /b 1
)

:: Run the main setup script
python "commanding\setup.py"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to execute the setup script.
    pause
    exit /b 1
)

echo [*] Setup completed successfully.
pause
