@echo off
cd /d "%~dp0"
echo Updating files...

curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/About.txt
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/LICENSE
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/ManagerPc.bat
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/README.md
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/desktop.ini
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/main.py
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/run.exe
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/setup.bat
curl -O https://raw.githubusercontent.com/wsl-iq/Manager-Pc/main/uninstall.py

echo Updating directories...
curl -L -o PackageMicroSoft.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/PackageMicroSoft.zip
curl -L -o commanding.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/commanding.zip
curl -L -o html.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/html.zip
curl -L -o icon.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/icon.zip
curl -L -o server.zip https://github.com/wsl-iq/Manager-Pc/archive/refs/heads/main/server.zip

powershell -command "Expand-Archive -Force 'PackageMicroSoft.zip' '.'"
powershell -command "Expand-Archive -Force 'commanding.zip' '.'"
powershell -command "Expand-Archive -Force 'html.zip' '.'"
powershell -command "Expand-Archive -Force 'icon.zip' '.'"
powershell -command "Expand-Archive -Force 'server.zip' '.'"

del PackageMicroSoft.zip
del commanding.zip
del html.zip
del icon.zip
del server.zip

echo Project update completed successfully!
pause
