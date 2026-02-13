#!/bin/bash
# 紧急部署脚本 - 使用GitHub Token方式

REPO_URL="https://github.com/leoxmrsh007/jiujing-academy.git"

echo "🚀 紧急部署 - 九经书院"
echo "======================="
echo ""

cd /mnt/d/Jiujing-Academy

echo "📋 当前状态:"
git status --short
echo ""

# 检查是否有token文件
if [ -f ".github-token" ]; then
    TOKEN=$(cat .github-token)
    echo "✅ 找到GitHub Token"
    
    # 使用token推送
    git remote set-url origin "https://leoxmrsh007:${TOKEN}@github.com/leoxmrsh007/jiujing-academy.git"
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ 部署成功！"
        echo "🌐 Vercel正在自动部署..."
    else
        echo "❌ 推送失败"
    fi
else
    echo "❌ 未找到GitHub Token"
    echo ""
    echo "请创建Personal Access Token:"
    echo "1. 访问 https://github.com/settings/tokens"
    echo "2. 点击 'Generate new token'"
    echo "3. 选择 'repo' 权限"
    echo "4. 复制token"
    echo "5. 粘贴到下面的文件:"
    echo "   D:\\Jiujing-Academy\\.github-token"
    echo ""
    read -p "按回车键退出..."
fi
