@echo off
chcp 65001
REM Jiujing Academy Vercel Deploy

echo ========================================
echo Jiujing Academy Deploy
echo ========================================
echo.

cd /d D:\Jiujing-Academy

echo Current directory: %CD%
echo.

REM Check vercel
vercel --version >nul 2>&1
if errorlevel 1 (
    echo Error: Vercel CLI not found
    echo Please install: npm install -g vercel
    pause
    exit /b 1
)

echo Vercel CLI found
echo.
echo Starting deployment...
echo.

REM Deploy
vercel --prod

echo.
echo ========================================
pause
