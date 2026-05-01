# 九经书院 Vercel 部署脚本
# 在Windows PowerShell中运行

cd D:\Jiujing-Academy

# 配置Git用户（避免权限问题）
git config user.email "huyong@jiujing.academy"
git config user.name "Yong Hu"

# 部署到Vercel个人项目
vercel --prod
