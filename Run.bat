@echo off
setlocal enabledelayedexpansion

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo Installing dependencies...

:: Install from requirements.txt
python -m pip install -r requirements.txt --index-url https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
if !errorlevel! neq 0 (
    python -m pip install -r requirements.txt
    if !errorlevel! neq 0 (
        echo Failed to install dependencies.
        pause
        exit /b 1
    )
)

:: Apply wxautox4 patch
python patch_wxautox4.py
if !errorlevel! neq 0 (
    echo wxautox4 patch failed, but continuing...
)

echo Dependencies installed!
cls

:: Kill existing process on port 5000
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5000') do (
    taskkill /F /PID %%a >nul 2>&1
)

:: Start config editor
start python config_editor.py

:: Open browser
start "" "http://localhost:5000"
