#!/bin/bash
# 启动本地服务器预览前端页面

echo "🚀 启动九经书院前端预览服务器"
echo ""

cd /mnt/d/Jiujing-Academy/frontend

# 检查Python是否可用
if command -v python3 &> /dev/null; then
    echo "📡 使用Python3启动服务器..."
    echo "🌐 访问地址: http://localhost:8080"
    echo "⏹️  按 Ctrl+C 停止服务器"
    echo ""
    python3 -m http.server 8080
elif command -v python &> /dev/null; then
    echo "📡 使用Python启动服务器..."
    echo "🌐 访问地址: http://localhost:8080"
    echo "⏹️  按 Ctrl+C 停止服务器"
    echo ""
    python -m http.server 8080
else
    echo "❌ 未找到Python，请手动安装"
    exit 1
fi
