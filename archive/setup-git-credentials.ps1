# GitHub免密推送配置（让我能自动部署）
# 在Windows PowerShell执行

Write-Host "配置GitHub自动推送（免密码）..." -ForegroundColor Green
Write-Host ""

cd D:\Jiujing-Academy

# 方法1: 使用Git Credential Manager（推荐）
Write-Host "方法1: 配置Git Credential Manager..." -ForegroundColor Yellow
Write-Host "这会保存你的GitHub凭据，允许免密推送" -ForegroundColor Cyan
Write-Host ""

git config --global credential.helper manager
git config --global user.name "Yong Hu"
git config --global user.email "huyong@jiujing.academy"

Write-Host "✅ 配置完成！" -ForegroundColor Green
Write-Host ""
Write-Host "下次推送时会要求输入一次用户名密码，" -ForegroundColor Cyan
Write-Host "之后就会自动保存，无需再输入。" -ForegroundColor Cyan
Write-Host ""
Write-Host "配置完成后，喵妹就能自动推送代码并部署了！" -ForegroundColor Green
