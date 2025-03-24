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
