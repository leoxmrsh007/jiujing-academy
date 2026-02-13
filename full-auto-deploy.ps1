# 九经书院全自动部署脚本（Windows管理员权限）
# 配置SSH免密后，以后自动部署无需输入密码

Write-Host "🔑 配置SSH免密推送..." -ForegroundColor Green
Write-Host "=====================" -ForegroundColor Green
Write-Host ""

# 生成SSH密钥（如果不存在）
$sshPath = "$env:USERPROFILE\.ssh\id_ed25519"
if (-not (Test-Path $sshPath)) {
    Write-Host "生成SSH密钥..." -ForegroundColor Yellow
    ssh-keygen -t ed25519 -C "huyong@jiujing.academy" -f $sshPath -N '""'
    Write-Host "✅ SSH密钥已生成" -ForegroundColor Green
} else {
    Write-Host "✅ SSH密钥已存在" -ForegroundColor Green
}

# 显示公钥
Write-Host ""
Write-Host "📋 请将以下公钥添加到GitHub:" -ForegroundColor Cyan
Write-Host "访问: https://github.com/settings/keys" -ForegroundColor Yellow
Write-Host ""
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub"
Write-Host ""

# 等待用户确认
Read-Host "添加完成后按回车键继续..."

# 测试SSH连接
Write-Host ""
Write-Host "🔄 测试SSH连接..." -ForegroundColor Yellow
ssh -T git@github.com 2>&1 | Out-Null
if ($LASTEXITCODE -eq 1) {
    Write-Host "✅ SSH连接成功！" -ForegroundColor Green
} else {
    Write-Host "⚠️ SSH连接测试失败，请检查密钥配置" -ForegroundColor Red
}

# 配置项目使用SSH
cd D:\Jiujing-Academy
Write-Host ""
Write-Host "🔧 配置项目使用SSH..." -ForegroundColor Yellow
git remote set-url origin git@github.com:leoxmrsh007/jiujing-academy.git
Write-Host "✅ 已切换为SSH方式" -ForegroundColor Green

# 推送代码
Write-Host ""
Write-Host "🚀 推送代码到GitHub..." -ForegroundColor Yellow
git push origin main
Write-Host ""
Write-Host "✅ 部署完成！" -ForegroundColor Green
Write-Host "🌐 Vercel将自动部署更新" -ForegroundColor Cyan
Write-Host ""
Read-Host "按回车键退出"
