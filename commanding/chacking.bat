@echo off

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    REM Python is installed, skip installation
    exit /b
) ELSE (
    REM Python is not installed, run the installer
    REM Replace "installer.exe" with your installer file name
    start /wait "" "python-3.11.0rc2.exe"
)

exit /b
