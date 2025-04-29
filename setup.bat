:: Custom License Based on MIT License
:: Update     : setup Packages Manager Pc
:: Version    : 3.2.1
:: Github     : https://github.com/wsl-iq/Manager-Pc
:: Developer  : Mohammed Al-Baqer



::                              Copyright (c) 2024-2025
::                              Version   : 3.2.1, 17 November 2024
::                              Developer : Mohammed Al-Baqer

:: ================================================================
::                        PRIVACY POLICY
::                    FOR MANAGER-PC PROJECT
:: ================================================================
::
:: Last Updated: April 29, 2025
::
:: This section provides transparency and confidence to all users of the 'Manager-Pc' application, particularly the 'setup.bat' script, regarding its behavior, data usage, and potential risks.
::
:: ---------------------------------------------------------------
:: 1. OVERVIEW
:: ---------------------------------------------------------------
:: 'Manager-Pc' is a personal utility developed to help users manage, optimize, and maintain their Windows system. It is distributed as an open-source tool under a permissive license.
::
:: The 'setup.bat' script is a component that facilitates the initial setup by executing necessary Python scripts and ensuring required packages are installed.
::
:: ---------------------------------------------------------------
:: 2. DATA COLLECTION & PRIVACY
:: ---------------------------------------------------------------
:: - This script DOES NOT collect, record, analyze, or send any data related to your identity, behavior, IP address, device, location, or files on your computer.
::
:: - The only activity this script performs is executing local Python scripts and installing necessary packages.
::
:: - NO information about your device or its usage is captured or shared at any time.
::
:: - There are NO cookies, tracking pixels, background telemetry, or any analytics embedded in this script or in any file it executes.
::
:: In short: Your privacy is 100% respected and preserved.
::
:: ---------------------------------------------------------------
:: 3. NETWORK COMMUNICATION
:: ---------------------------------------------------------------
:: The script may initiate network communication solely for the purpose of installing or upgrading Python packages using pip. This involves contacting the Python Package Index (PyPI) to fetch the latest versions of required packages.
::
:: No other external URLs, APIs, web services, or hidden endpoints are contacted under any circumstances.
::
:: ---------------------------------------------------------------
:: 4. THIRD-PARTY SERVICES
:: ---------------------------------------------------------------
:: The setup process does NOT use any third-party services like:
:: - Google APIs
:: - Microsoft telemetry
:: - Cloud analytics platforms
:: - Webhooks or callbacks
::
:: All operations are self-contained and do not rely on any external service provider besides PyPI, which is used for package management.
::
:: ---------------------------------------------------------------
:: 5. SECURITY AND SAFETY
:: ---------------------------------------------------------------
:: We strongly believe in giving the user full control and understanding over what happens on their system. Therefore:
::
:: - Scripts are executed only with the user's consent.
:: - The script does not modify your registry, background tasks, startup entries, or system settings beyond what's necessary for the setup.
:: - You are encouraged to manually review the content of scripts and packages before execution.
:: - You should run the script in an environment where you have administrator rights to prevent permission issues, but this does not imply the script elevates itself silently.
::
:: Safety Tips:
:: > Always verify that the source repository is correct.
:: > Avoid running the script if you suspect any tampering.
:: > Use antivirus tools to scan newly downloaded packages if you're concerned.
::
:: ---------------------------------------------------------------
:: 6. USER RESPONSIBILITY
:: ---------------------------------------------------------------
:: By choosing to run this script, you understand and agree that:
::
:: - You are manually initiating the setup process.
:: - You acknowledge and accept what scripts are being executed.
:: - You agree that the developer is not responsible for system issues caused by misuse, external modifications, or running the script in compromised environments.
::
:: This script is provided **as-is** and is intended for educational and system utility purposes only.
::
:: ---------------------------------------------------------------
:: 7. CHANGES TO THIS POLICY
:: ---------------------------------------------------------------
:: This privacy notice may be revised from time to time.
:: If so, the updated version will always appear within this comment block in the script itself.
::
:: It is recommended to re-check this policy after each update.
::
:: ---------------------------------------------------------------
:: 8. CONTACT INFORMATION
:: ---------------------------------------------------------------
:: If you have any concerns, suggestions, or questions regarding:
:: - Privacy practices
:: - Script behavior
:: - Setup security
::
:: Please reach out via:
:: >> GitHub Issues page: https://github.com/wsl-iq/Manager-Pc/issues
:: >> OR insert your official email/contact method here.
::
:: ================================================================
::                  END OF PRIVACY POLICY
:: ================================================================


:: ================================================================
:: [ Conclusion]
:: ================================================================

:: Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
:: (the "Software"), to use modify, and distribute modified versions of the Software **for personal or educational purposes only**, 
:: provided that the following conditions are met:

:: 1. The Software **may not be used, sold, or resold for commercial purposes** in any form, whether directly or indirectly.
:: 2. This copyright notice must be retained in all copies and significant modifications.
:: 3. Any modified version must acknowledge the original developer.
:: 4. Unauthorized distribution of the original or modified versions **for financial gain** is strictly prohibited.
:: 5. This license does not grant permission to use the Software for any illegal activities.
:: 6. The developer is not responsible for providing ongoing support, updates, or maintenance.

:: THE SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND EXPRESS OR IMPLIED INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
:: IN NO EVENT SHALL THE AUTHOR OR COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM DAMAGES OR OTHER LIABILITY WHETHER IN AN ACTION OF CONTRACT TORT OR OTHERWISE ARISING FROM OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

:: ================================================================
::                  END OF PRIVACY POLICY
:: ================================================================


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
