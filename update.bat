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
:: IMPORTANT: This section is intended to provide complete
:: transparency and confidence to all users of the 'Manager-Pc'
:: application, particularly the 'update.bat' script, regarding
:: how it behaves, what data it uses, and what risks (if any)
:: are involved.
::
:: ---------------------------------------------------------------
:: 1. OVERVIEW
:: ---------------------------------------------------------------
:: 'Manager-Pc' is a personal utility developed to help users
:: manage, optimize, and maintain their Windows system. It is
:: distributed as an open-source tool under a permissive license.
::
:: The 'update.bat' script is a critical component that allows the
:: application to stay current by automatically downloading the 
:: latest version of its essential files from the official GitHub 
:: repository. It ensures the user always has access to the most
:: updated tools, bug fixes, and improvements without needing to
:: manually track changes.
::
:: ---------------------------------------------------------------
:: 2. DATA COLLECTION & PRIVACY
:: ---------------------------------------------------------------
:: - This script DOES NOT collect, record, analyze, or send any
::   data related to your identity, behavior, IP address, device,
::   location, or files on your computer.
::
:: - The only activity this script performs is downloading static
::   files (text, scripts, executables, configurations) directly
::   from a public GitHub repository.
::
:: - NO information about your device or its usage is captured or
::   shared at any time.
::
:: - There are NO cookies, tracking pixels, background telemetry,
::   or any analytics embedded in this script or in any file it
::   downloads.
::
:: In short: Your privacy is 100% respected and preserved.

:: ---------------------------------------------------------------
:: 3. NETWORK COMMUNICATION
:: ---------------------------------------------------------------
:: The script makes use of the `curl` command to perform HTTP/HTTPS
:: GET requests for downloading the following files:
::
:: - LICENSE
:: - ManagerPc.bat
:: - README.md
:: - desktop.ini
:: - main.py
:: - run.exe
:: - setup.bat
:: - uninstall.py
:: - update.py
:: - PackageMicroSoft.zip
::
:: Each file is retrieved directly from:
:: https://github.com/wsl-iq/Manager-Pc
::
:: This is a public, transparent GitHub repository. No external
:: URLs, APIs, web services, or hidden endpoints are contacted
:: under any circumstances.

:: ---------------------------------------------------------------
:: 4. THIRD-PARTY SERVICES
:: ---------------------------------------------------------------
:: The update process does NOT use any third-party services like:
:: - Google APIs
:: - Microsoft telemetry
:: - Cloud analytics platforms
:: - Webhooks or callbacks
::
:: All operations are self-contained and do not rely on any
:: external service provider besides GitHub, which simply hosts
:: the code files.

:: ---------------------------------------------------------------
:: 5. SECURITY AND SAFETY
:: ---------------------------------------------------------------
:: We strongly believe in giving the user full control and
:: understanding over what happens on their system. Therefore:
::
:: - Files are downloaded **only**, not executed automatically.
:: - The script does not modify your registry, background tasks,
::   startup entries, or system settings.
:: - You are encouraged to manually open and verify the content
::   of downloaded files before running them.
:: - You should run the script in an environment where you have
::   administrator rights to prevent permission issues, but this
::   does not imply the script elevates itself silently.
::
:: Safety Tips:
:: > Always verify that the source GitHub repository is correct.
:: > Avoid running the script if you suspect any tampering.
:: > Use antivirus tools to scan newly downloaded executables
::   if you're concerned.

:: ---------------------------------------------------------------
:: 6. USER RESPONSIBILITY
:: ---------------------------------------------------------------
:: By choosing to run this script, you understand and agree that:
::
:: - You are manually initiating the update process.
:: - You acknowledge and accept what files are being replaced.
:: - You agree that the developer is not responsible for system
::   issues caused by misuse, external modifications, or running
::   the script in compromised environments.
::
:: This script is provided **as-is** and is intended for educational
:: and system utility purposes only.

:: ---------------------------------------------------------------
:: 7. CHANGES TO THIS POLICY
:: ---------------------------------------------------------------
:: This privacy notice may be revised from time to time.
:: If so, the updated version will always appear within this
:: comment block in the script itself.
::
:: It is recommended to re-check this policy after each update.

:: ---------------------------------------------------------------
:: 8. CONTACT INFORMATION
:: ---------------------------------------------------------------
:: If you have any concerns, suggestions, or questions regarding:
:: - Privacy practices
:: - File behavior
:: - Update security
::
:: Please reach out via:
:: >> GitHub Issues page: https://github.com/wsl-iq/Manager-Pc/issues
:: >> OR insert your official email/contact method here.

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
cd /d "%~dp0"

echo Updating files...

curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/LICENSE
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/ManagerPc.bat
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/README.md
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/desktop.ini
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/main.py
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/run.exe
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/setup.bat
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/uninstall.py
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/update.py

echo Finish Update Files 

echo Updating directories...

curl -L -o PackageMicroSoft.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/PackageMicroSoft.zip
curl -L -o Banner.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/Banner.zip
curl -L -o Application.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/Application.zip
curl -L -o Project.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/Project.zip
curl -L -o commanding.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/commanding.zip
curl -L -o html.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/html.zip
curl -L -o icon.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/icon.zip
curl -L -o server.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/server.zip

echo Finish Update Folders or directories

echo Unzipping files...

powershell -command "Expand-Archive -Force 'PackageMicroSoft.zip' '.'"
powershell -command "Expand-Archive -Force 'Project.zip' '.'"
powershell -command "Expand-Archive -Force 'Application.zip' '.'"
powershell -command "Expand-Archive -Force 'Banner.zip' '.'"
powershell -command "Expand-Archive -Force 'commanding.zip' '.'"
powershell -command "Expand-Archive -Force 'html.zip' '.'"
powershell -command "Expand-Archive -Force 'icon.zip' '.'"
powershell -command "Expand-Archive -Force 'server.zip' '.'"

echo Finish UnZip Folders

echo Removing temporary files...

del PackageMicroSoft.zip
del commanding.zip
del Application.zip
del Project.zip
del Banner.zip
del html.zip
del icon.zip
del server.zip

echo Cleaning temporary files...
del /q /s /f "%temp%\*"
cleanmgr /sagerun:1

echo Project update completed successfully!

set /p choice=Do you want to restart the computer? (Y/N): 

if /I "%choice%"=="Y" goto restart
if /I "%choice%"=="N" goto cancel

echo Invalid choice, please enter Y or N.
pause
exit

:restart
echo The computer will restart in 5 seconds...
timeout /t 5 /nobreak >nul
shutdown /r /t 0
exit

:cancel
echo Operation canceled.
pause
exit
