# 强制更新 vercel.json 脚本
# 在 PowerShell 中执行

cd D:\Jiujing-Academy

# 方法1: 强制添加
git add -f vercel.json
git status

# 方法2: 如果方法1无效，尝试修改时间戳
# (Get-Item vercel.json).LastWriteTime = Get-Date

# 方法3: 重新创建文件
# Copy-Item vercel.json vercel.json.bak
# Remove-Item vercel.json
# Move-Item vercel.json.bak vercel.json

git add vercel.json
git commit -m "fix: 修复路由配置，解决点击无效问题"
git push

Write-Host "推送完成！"
