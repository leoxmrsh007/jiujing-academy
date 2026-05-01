# 九经书院自动部署配置（leoxmrsh007专用）
# 在Windows PowerShell中运行

Write-Host "🚀 九经书院自动部署配置" -ForegroundColor Green
Write-Host "========================" -ForegroundColor Green
Write-Host ""

# 进入项目目录
cd D:\Jiujing-Academy

Write-Host "步骤1: 配置Git..." -ForegroundColor Yellow
git config user.name "Yong Hu"
git config user.email "huyong@jiujing.academy"
Write-Host "✅ Git配置完成" -ForegroundColor Green
Write-Host ""

Write-Host "步骤2: 提交最新代码..." -ForegroundColor Yellow
git add -A
git commit -m "v0.3.1: 添加点击跳转功能 + 页面优化"
Write-Host "✅ 代码已提交" -ForegroundColor Green
Write-Host ""

Write-Host "步骤3: 连接GitHub仓库..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin https://github.com/leoxmrsh007/jiujing-academy.git
git branch -M main
Write-Host "✅ 仓库连接完成" -ForegroundColor Green
Write-Host ""

Write-Host "步骤4: 推送代码到GitHub..." -ForegroundColor Yellow
Write-Host "（会提示输入GitHub用户名和密码/Token）" -ForegroundColor Cyan
git push -u origin main --force
Write-Host "✅ 代码已推送到GitHub" -ForegroundColor Green
Write-Host ""

Write-Host "步骤5: 配置Vercel自动部署..." -ForegroundColor Yellow
Write-Host ""
Write-Host "请访问: https://vercel.com/new" -ForegroundColor Cyan
Write-Host "1. 点击 'Import Git Repository'" -ForegroundColor White
Write-Host "2. 选择 'leoxmrsh007/jiujing-academy'" -ForegroundColor White
Write-Host "3. 点击 'Deploy'" -ForegroundColor White
Write-Host ""
Write-Host "✅ 完成后，每次git push都会自动部署！" -ForegroundColor Green
Write-Host ""
Read-Host "按回车键退出"
