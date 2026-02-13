# GitHub免密推送配置脚本
# 在Windows PowerShell中运行（管理员权限）

Write-Host "🔑 配置GitHub免密推送..." -ForegroundColor Green
Write-Host "========================" -ForegroundColor Green
Write-Host ""

cd D:\Jiujing-Academy

Write-Host "步骤1: 配置Git凭证管理器..." -ForegroundColor Yellow

# 启用Git Credential Manager
git config --global credential.helper manager-core

# 配置用户信息
git config --global user.name "Yong Hu"
git config --global user.email "huyong@jiujing.academy"

Write-Host "✅ Git配置完成" -ForegroundColor Green
Write-Host ""

Write-Host "步骤2: 测试免密推送..." -ForegroundColor Yellow
Write-Host "（会提示输入一次用户名和密码，之后自动保存）" -ForegroundColor Cyan
Write-Host ""

# 创建测试提交
echo "# Auto Deploy Test" >> README.md
git add README.md
git commit -m "测试自动部署配置"

# 推送（会提示输入凭据，保存后下次免密）
git push origin main

Write-Host ""
Write-Host "✅ 配置完成！" -ForegroundColor Green
Write-Host ""
Write-Host "下次推送时将不再需要输入密码。" -ForegroundColor Cyan
Write-Host "喵妹现在可以自动部署了！🐱" -ForegroundColor Green
