:: Custom License Based on MIT License
:: Update     : Update Programming Manager Pc
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
:: This section provides transparency and confidence to all users of the 'Manager-Pc' application, particularly the 'python-3.11.0rc2-amd64.bat' script, regarding its behavior, data usage, and potential risks.
::
:: ---------------------------------------------------------------
:: 1. OVERVIEW
:: ---------------------------------------------------------------
:: The 'python-3.11.0rc2-amd64.bat' script is designed to automate the installation of Python 3.11.0 Release Candidate 2 on Windows systems. It simplifies the setup process by downloading the official installer and executing it with predefined parameters.
::
:: ---------------------------------------------------------------
:: 2. DATA COLLECTION & PRIVACY
:: ---------------------------------------------------------------
:: - This script DOES NOT collect, record, analyze, or send any data related to your identity, behavior, IP address, device, location, or files on your computer.
::
:: - The only activity this script performs is downloading the official Python installer and executing it locally.
::
:: - NO information about your device or its usage is captured or shared at any time.
::
:: - There are NO cookies, tracking pixels, background telemetry, or any analytics embedded in this script or in any file it downloads.
::
:: In short: Your privacy is 100% respected and preserved.
::
:: ---------------------------------------------------------------
:: 3. NETWORK COMMUNICATION
:: ---------------------------------------------------------------
:: The script initiates a network connection solely to download the official Python 3.11.0rc2 installer from the Python Software Foundation's website:
::
:: - URL: https://www.python.org/ftp/python/3.11.0rc2/python-3.11.0rc2-amd64.exe
::
:: No other external URLs, APIs, web services, or hidden endpoints are contacted under any circumstances.
::
:: ---------------------------------------------------------------
:: 4. THIRD-PARTY SERVICES
:: ---------------------------------------------------------------
:: The installation process does NOT use any third-party services like:
:: - Google APIs
:: - Microsoft telemetry
:: - Cloud analytics platforms
:: - Webhooks or callbacks
::
:: All operations are self-contained and do not rely on any external service provider besides the official Python website.
::
:: ---------------------------------------------------------------
:: 5. SECURITY AND SAFETY
:: ---------------------------------------------------------------
:: We strongly believe in giving the user full control and understanding over what happens on their system. Therefore:
::
:: - The installer is sourced directly from the official Python website, ensuring authenticity.
:: - The script executes the installer with silent installation parameters, avoiding unnecessary prompts.
:: - The script does not modify your registry, background tasks, startup entries, or system settings beyond what's necessary for the Python installation.
:: - You are encouraged to manually verify the authenticity of the downloaded installer before execution.
:: - It is recommended to run the script in an environment where you have administrator rights to prevent permission issues, but this does not imply the script elevates itself silently.
::
:: Safety Tips:
:: > Always verify that the source URL is correct and points to the official Python website.
:: > Avoid running the script if you suspect any tampering.
:: > Use antivirus tools to scan the downloaded installer if you're concerned.
::
:: ---------------------------------------------------------------
:: 6. USER RESPONSIBILITY
:: ---------------------------------------------------------------
:: By choosing to run this script, you understand and agree that:
::
:: - You are manually initiating the Python installation process.
:: - You acknowledge and accept the changes made to your system by the Python installer.
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
:: - Installation security
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
