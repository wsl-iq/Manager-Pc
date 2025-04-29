:: Custom License Based on MIT License
:: Update     : FixBug Programming Manager Pc
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
:: This section provides transparency and confidence to all users of the 'Manager-Pc' application, particularly the 'FixBug.cmd' script, regarding its behavior, data usage, and potential risks.
::
:: ---------------------------------------------------------------
:: 1. OVERVIEW
:: ---------------------------------------------------------------
:: The 'FixBug.cmd' script is designed to address and rectify known issues within the 'Manager-Pc' application. It automates specific corrective actions to ensure optimal functionality and user experience.
::
:: ---------------------------------------------------------------
:: 2. DATA COLLECTION & PRIVACY
:: ---------------------------------------------------------------
:: - This script DOES NOT collect, record, analyze, or send any data related to your identity, behavior, IP address, device, location, or files on your computer.
::
:: - The only activity this script performs is executing predefined commands to fix specific issues within the application.
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
:: The script does NOT initiate any network connections. All operations are performed locally on your machine without contacting external servers or services.
::
:: ---------------------------------------------------------------
:: 4. THIRD-PARTY SERVICES
:: ---------------------------------------------------------------
:: The 'FixBug.cmd' script does NOT utilize any third-party services or tools. All actions are executed using native Windows commands and functionalities.
::
:: ---------------------------------------------------------------
:: 5. SECURITY AND SAFETY
:: ---------------------------------------------------------------
:: We strongly believe in giving the user full control and understanding over what happens on their system. Therefore:
::
:: - The script performs only the necessary actions required to fix known issues within the application.
:: - It does not modify your registry, background tasks, startup entries, or system settings beyond what's necessary for the fix.
:: - You are encouraged to manually review the content of the script before execution.
:: - It is recommended to run the script in an environment where you have administrator rights to prevent permission issues, but this does not imply the script elevates itself silently.
::
:: Safety Tips:
:: > Always verify that the source of the script is trusted.
:: > Avoid running the script if you suspect any tampering.
:: > Use antivirus tools to scan the script if you're concerned.
::
:: ---------------------------------------------------------------
:: 6. USER RESPONSIBILITY
:: ---------------------------------------------------------------
:: By choosing to run this script, you understand and agree that:
::
:: - You are manually initiating the fix process.
:: - You acknowledge and accept the changes made to your system by the script.
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
:: - Fix process security
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




@echo off
:: Check if the script is running as Administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting Administrator privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs"
    exit
)

echo Developer [Mohammed Al-Baqer] 
echo.
title Windows Fix Tool
color 0A
echo     Windows Repair Tool
echo.

:: Clean up unnecessary files
echo Cleaning temporary files...
del /s /q %temp%\*.* 
del /s /q C:\Windows\Temp\*.*

:: Repair system image using DISM
echo Repairing Windows image using DISM...
DISM /Online /Cleanup-image /RestoreHealth

:: Reset network services
echo Resetting network settings...
netsh winsock reset
netsh int ip reset

:: Check and fix disk errors
echo Checking and fixing disk errors...
chkdsk C: /f /r /x

:: Flush DNS cache
echo Flushing DNS cache...
ipconfig /flushdns

echo.
echo The process is complete! It's recommended to restart your computer.
pause
exit
