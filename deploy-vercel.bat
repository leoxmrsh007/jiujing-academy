@echo off
chcp 65001
REM 九经书院 Vercel 部署脚本
REM 请在Windows中双击运行

echo ========================================
echo 🚀 九经书院 Vercel 部署
echo ========================================
echo.

REM 进入项目目录
cd /d D:\Jiujing-Academy

echo 📁 项目目录: %CD%
echo.

REM 检查vercel
where vercel >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Vercel CLI 未安装
    echo 请先运行: npm install -g vercel
    pause
    exit /b 1
)

echo ✅ Vercel CLI 已安装
echo.

REM 部署
echo 🚀 开始部署到生产环境...
echo.
vercel --prod

echo.
echo ========================================
pause
