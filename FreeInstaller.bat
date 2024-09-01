@echo off

set PYTHON_VERSION=3.12.0
set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set GITHUB_REPO=https://github.com/UniDCYT/Advanced-IF-Download-Version/archive/refs/heads/main.zip
set TARGET_DIR=%localappdata%\AdvancedIF
set TARGET_FILE=Advanced IF.py
set SHORTCUT_NAME=Advanced IF.lnk
set SHORTCUT_PATH=%USERPROFILE%\Desktop\%SHORTCUT_NAME%
set ICON_PATH=%TARGET_DIR%\Icon.ico
set TARGET_FILE_PATH=%TARGET_DIR%\%TARGET_FILE%

if exist "%TARGET_DIR%" (
    echo Deleting existing files in %TARGET_DIR%...
    rmdir /s /q "%TARGET_DIR%"
)

echo Downloading Python %PYTHON_VERSION% installer...
curl -o %PYTHON_INSTALLER% https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%
start /wait "" "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1

python --version || (
    echo Python installation failed!
    exit /b 1
)

python -m pip install --upgrade pip
python -m pip install pillow requests pywin32 pyperclip

if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
)

echo Downloading repository files...
curl -L -o repo.zip %GITHUB_REPO%
powershell -command "Expand-Archive -Path 'repo.zip' -DestinationPath '%TARGET_DIR%' -Force"

move "%TARGET_DIR%\Advanced-IF-Download-Version-main\*" "%TARGET_DIR%\"
rmdir /s /q "%TARGET_DIR%\Advanced-IF-Download-Version-main"

del repo.zip

if not exist "%ICON_PATH%" (
    echo Icon file not found at %ICON_PATH%.
    echo Ensure the icon file exists or update the ICON_PATH variable.
    pause
    exit /b 1
)

echo Set WshShell = WScript.CreateObject("WScript.Shell") > "%temp%\CreateShortcut.vbs"
echo Set Shortcut = WshShell.CreateShortcut("%SHORTCUT_PATH%") >> "%temp%\CreateShortcut.vbs"
echo Shortcut.TargetPath = "%TARGET_FILE_PATH%" >> "%temp%\CreateShortcut.vbs"
echo Shortcut.WorkingDirectory = "%TARGET_DIR%" >> "%temp%\CreateShortcut.vbs"
echo Shortcut.IconLocation = "%ICON_PATH%" >> "%temp%\CreateShortcut.vbs"
echo Shortcut.Save >> "%temp%\CreateShortcut.vbs"

cscript /nologo "%temp%\CreateShortcut.vbs"

del "%temp%\CreateShortcut.vbs"

echo Shortcut with icon created on desktop.
pause
