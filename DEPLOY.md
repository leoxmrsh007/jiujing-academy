# Vercel 部署指南

## 一键部署

### 方法1: Vercel CLI (推荐)

```bash
# 1. 进入项目目录
cd /mnt/d/Jiujing-Academy

# 2. 安装 Vercel CLI (如未安装)
npm i -g vercel

# 3. 登录 Vercel
vercel login

# 4. 部署
vercel --prod
```

### 方法2: GitHub + Vercel (自动部署)

1. 在GitHub创建仓库
2. 推送代码: `git push origin main`
3. 在 Vercel dashboard 导入项目
4. 自动部署完成！

### 方法3: Vercel Dashboard 手动上传

1. 访问 https://vercel.com/new
2. 选择 "Import Git Repository" 或 "Upload"
3. 选择九经书院项目
4. 点击 Deploy

---

## 配置说明

### vercel.json
- 静态网站部署配置
- 路由规则: 所有路径指向 frontend/index.html
- 缓存策略: 1小时

### 部署后地址
部署完成后会获得:
- `https://jiujing-academy-xxx.vercel.app` (生产环境)
- `https://jiujing-academy-xxx-git-main-xxx.vercel.app` (预览环境)

### 自定义域名 (可选)
1. 在 Vercel Dashboard → Settings → Domains
2. 添加你的域名
3. 按提示配置 DNS

---

## 项目结构

```
Jiujing-Academy/
├── frontend/
│   └── index.html          # 主页面
├── backend/                # API (可选)
├── vercel.json             # Vercel配置
├── package.json            # 项目信息
└── README.md
```

---

**版本**: v0.2.0  
**部署时间**: 2026-02-13
