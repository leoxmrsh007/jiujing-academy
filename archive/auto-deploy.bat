@echo off
chcp 65001
echo 🚀 九经书院自动部署
echo ===================
echo.

cd /d D:\Jiujing-Academy

echo 📦 检查更新...
git status --short

echo.
echo 📤 推送到GitHub...
git push origin main

echo.
echo ✅ 推送完成！
echo 🌐 Vercel将自动部署更新
echo.
echo 请访问 https://vercel.com/dashboard 查看部署状态
pause
