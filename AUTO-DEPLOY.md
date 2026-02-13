# 自动部署配置指南

## 方案：Vercel + GitHub 自动部署

### 步骤1: 创建GitHub仓库
1. 访问 https://github.com/new
2. 仓库名: `jiujing-academy`
3. 选择 Public（公开）或 Private（私有）
4. 点击 "Create repository"

### 步骤2: 推送代码到GitHub
```bash
cd D:\Jiujing-Academy
git remote add origin https://github.com/YOUR_USERNAME/jiujing-academy.git
git branch -M main
git push -u origin main
```

### 步骤3: Vercel连接GitHub
1. 访问 https://vercel.com/new
2. 点击 "Import Git Repository"
3. 选择 `jiujing-academy` 仓库
4. 点击 "Deploy"

### 完成！✅
现在每次你提交代码到GitHub，Vercel会自动部署！

---

## 自动部署工作流

```
你提交代码 → GitHub收到 → Vercel自动部署 → 网站更新
    ↑                                                    ↓
    └──────────────── 无需人工干预 ──────────────────────┘
```

### 后续更新只需：
```bash
git add .
git commit -m "更新内容"
git push
# Vercel自动部署，无需手动操作！
```

---

## 快速命令

### 一键提交并自动部署
```bash
cd D:\Jiujing-Academy
git add -A
git commit -m "更新"
git push
# 等待Vercel自动部署（约1-2分钟）
```

### 查看部署状态
访问 https://vercel.com/dashboard 查看部署进度

---

*配置时间: 2026-02-13*
