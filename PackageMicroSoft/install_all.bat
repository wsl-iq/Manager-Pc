@echo off
CD /d %~dp0

echo.
echo Microsoft Visual C++ All-In-One Runtimes by Mohammed Al-Baqer
echo.
echo Installing runtime packages...

set IS_X64=0 && if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (set IS_X64=1) else (if "%PROCESSOR_ARCHITEW6432%"=="AMD64" (set IS_X64=1))

if "%IS_X64%" == "1" goto X64
goto END

:X64

echo 2015 - 2022...
start /wait vcredist2015_2017_2019_2022_x64.exe /passive /norestart

goto END

:END

echo.
echo Installation completed successfully
exit