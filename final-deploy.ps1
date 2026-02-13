# 最后部署步骤（Windows PowerShell）

Write-Host "🚀 最终部署..." -ForegroundColor Green

# 配置SSH
$env:GIT_SSH_COMMAND = "ssh -o StrictHostKeyChecking=no"

# 切换到项目目录
cd D:\Jiujing-Academy

# 配置使用SSH
git remote set-url origin git@github.com:leoxmrsh007/jiujing-academy.git

# 推送代码
Write-Host "📤 推送代码..." -ForegroundColor Yellow
git push origin main

Write-Host ""
Write-Host "✅ 部署完成！" -ForegroundColor Green
