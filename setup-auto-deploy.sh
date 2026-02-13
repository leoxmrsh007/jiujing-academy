#!/bin/bash
# 九经书院自动部署配置脚本
# 在Git Bash或WSL中运行

echo "🚀 九经书院自动部署配置"
echo "========================"
echo ""

# 检查是否在正确目录
if [ ! -f "frontend/index.html" ]; then
    echo "❌ 错误：请在Jiujing-Academy目录中运行此脚本"
    exit 1
fi

echo "步骤1: 检查Git配置..."
git config user.name "Yong Hu"
git config user.email "huyong@jiujing.academy"
echo "✅ Git配置完成"
echo ""

echo "步骤2: 准备提交代码..."
git add -A
git commit -m "v0.3.1: 添加点击跳转功能" 2>/dev/null || echo "无新更改"
echo "✅ 代码已提交"
echo ""

echo "步骤3: 连接GitHub仓库..."
read -p "请输入你的GitHub用户名: " USERNAME

REPO_URL="https://github.com/$USERNAME/jiujing-academy.git"

echo ""
echo "请在浏览器中完成以下操作："
echo ""
echo "1. 访问: https://github.com/new"
echo "2. 仓库名: jiujing-academy"
echo "3. 点击 'Create repository'"
echo ""
echo "完成后按回车继续..."
read

echo "步骤4: 推送代码到GitHub..."
git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
git branch -M main
git push -u origin main

echo ""
echo "步骤5: 配置Vercel自动部署..."
echo ""
echo "请访问: https://vercel.com/new"
echo "1. 点击 'Import Git Repository'"
echo "2. 选择 'jiujing-academy' 仓库"
echo "3. 点击 'Deploy'"
echo ""
echo "✅ 完成后，每次git push都会自动部署！"
echo ""
