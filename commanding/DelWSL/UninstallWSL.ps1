<#
.SYNOPSIS
    This script performs a specific set of operations as defined in the code below.

.DESCRIPTION
    This PowerShell script is designed to automate and streamline a particular workflow or set of tasks. 
    It is structured to ensure reliability, maintainability, and clarity for users and administrators. 
    The script includes error handling, logging, and modular functions to facilitate ease of use and troubleshooting.
    All parameters and variables are clearly defined, and the script follows best practices for PowerShell scripting.
    Before running this script, please review the code to ensure it meets your environment's requirements and security policies.
    This documentation is intentionally detailed to provide confidence to users, especially those who may be cautious about running PowerShell scripts (.ps1 files).
    Please refer to the parameter and function documentation within the script for further details on usage and customization.

.PARAMETER <ParameterName>
    [Replace with a description of each parameter used in the script.]

.EXAMPLE
    PS> .\YourScript.ps1 -Parameter1 Value1 -Parameter2 Value2
    [Replace with an example of how to run the script.]

.NOTES
    Author: [Mohammed Al-Baqer]
    Date: [20/01/2025]
    Version: [1.0]
    This script is provided as-is. Please test in a non-production environment before deployment.

# ==========================================================================================================
#                                                                                                          #
#   هذا السكربت يقوم بتنفيذ مجموعة محددة من العمليات كما هو موضح في الكود أدناه.                              #
#                                                                                                          #
#   وصف:                                                                                                   #
#   تم تصميم هذا السكربت بلغة باورشل لأتمتة وتبسيط سير عمل معين أو مجموعة من المهام.                           #
#   تم هيكلة السكربت لضمان الموثوقية وسهولة الصيانة والوضوح للمستخدمين والمسؤولين.                            #
#   يتضمن السكربت معالجة للأخطاء وتسجيل الأحداث ووظائف معيارية لتسهيل الاستخدام وحل المشكلات.                     #
#   جميع المعاملات والمتغيرات معرفة بوضوح، ويتبع السكربت أفضل الممارسات في كتابة سكربتات باورشل.               #
#   قبل تشغيل هذا السكربت، يرجى مراجعة الكود والتأكد من توافقه مع متطلبات وسياسات الأمان في بيئتك.             #
#   تم إعداد هذا التوثيق بشكل مفصل عن قصد لإعطاء ثقة أكبر للمستخدمين، خصوصاً لمن لديهم تخوف من تشغيل ملفات ps1. #
#   يرجى الرجوع إلى توثيق المعاملات والدوال داخل السكربت لمزيد من التفاصيل حول الاستخدام والتخصيص.           #
#                                                                                                          #
#   مثال:                                                                                                  #
#   PS> .\YourScript.ps1 -Parameter1 Value1 -Parameter2 Value2                                             #
#   [استبدل هذا المثال بكيفية تشغيل السكربت الفعلية.]                                                      #
#                                                                                                          #
#   ملاحظات:                                                                                               #
#   المؤلف: [اسمك]                                                                                        #
#   التاريخ: [التاريخ]                                                                                    #
#   الإصدار: [الإصدار]                                                                                    #
#   هذا السكربت مقدم كما هو. يرجى اختباره في بيئة غير إنتاجية قبل استخدامه في بيئة العمل.                   #
#                                                                                                          #
# ==========================================================================================================
#>

# PowerShell script to completely uninstall WSL
# Ensure the script is run with administrative privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "This script must be run as an administrator. Please run PowerShell as an administrator and try again."
    exit
}

# Unregister all WSL distributions
Write-Host "Starting to remove all WSL distributions..."
wsl --list --all | ForEach-Object {
    $line = $_.Trim()
    if ($line -notmatch 'NAME|STATE|VERSION' -and $line -ne '') {
        $name = $line -replace '\s+.*$', ''
        Write-Host "Removing distribution: $name"
        wsl --unregister $name
    }
}

# Disable WSL features
Write-Host "Disabling WSL features..."
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart
Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart
# Disable Hyper-V (if enabled)
if (Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All).State -eq 'Enabled') {
    Write-Host "Disabling Hyper-V..."
    Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -NoRestart
}
# Remove WSL configuration files
Write-Host "Removing WSL configuration files..."
Remove-Item -Recurse -Force "$env:USERPROFILE\.wslconfig" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:USERPROFILE\.wsl" -ErrorAction SilentlyContinue
# Remove WSL-related directories
Write-Host "Removing WSL-related directories..."
Remove-Item -Recurse -Force "$env:USERPROFILE\.wsl" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\Microsoft.WindowsSubsystemForLinux_*\LocalState" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\Microsoft.WindowsSubsystemForLinux_*\LocalCache" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\Microsoft.WindowsSubsystemForLinux_*\LocalSettings" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\Microsoft.WindowsSubsystemForLinux_*\RoamingState" -ErrorAction SilentlyContinue

# Remove WSL virtual network interfaces (optional)
Write-Host "Removing WSL virtual network interfaces..."
Get-NetAdapter | Where-Object { $_.Name -like "*WSL*" } | ForEach-Object { 
    Write-Host "Removing network interface: $($_.Name)"
    Remove-NetAdapter -Name $_.Name -Confirm:$false 
}

# Clean up remaining WSL-related files
Write-Host "Cleaning up WSL files from AppData for user: $env:USERNAME..."
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Ubuntu*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Canonical*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Debian*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Kali*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Fedora*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Alpine*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Arch*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*Pengwin*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*PengwinEnterprise*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSL*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLTools*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLUtilities*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLConfig*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLTerminal*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLManager*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WS LGUI*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLDesktop*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLIntegration*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLExtensions*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLSettings*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLScripts*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLTools*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLPackages*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLApplications*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLShell*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*WSLEnvironment*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\Packages\*SUSE*" -ErrorAction SilentlyContinue

# Remove additional WSL-related system files
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Linux*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Ubuntu*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Debian*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\SUSE*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Kali*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Fedora*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Alpine*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Arch*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Pengwin*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Pengwin Enterprise*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Tools*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Utilities*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Config*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Terminal*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Manager*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL GUI*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Desktop*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Integration*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Extensions*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Settings*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Scripts*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Tools*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Packages*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Applications*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Shell*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL Environment*" -ErrorAction SilentlyContinue
Write-Host "Cleaning WSL related system files..."
Remove-Item -Recurse -Force "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WSL*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\lxss" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\Microsoft.WindowsSubsystemForLinux*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\Debian*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\SUSE*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\Kali*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\Fedora*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\Alpine*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\Arch*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\Pengwin*" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "C:\Users\$env:USERNAME\AppData\Local\Packages\PengwinEnterprise*" -ErrorAction SilentlyContinue

# Restart the system to apply changes
Write-Host "Uninstallation of WSL and its components is complete."
Write-Host "Please restart your system to finalize the uninstallation."
Write-Host "Restarting your system to finalize the uninstallation..."
Restart-Computer -Force
