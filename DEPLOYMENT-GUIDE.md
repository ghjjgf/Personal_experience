# 网页部署指南

## 🚀 部署到 GitHub Pages（推荐）

### 第一步：创建 GitHub 账号

如果您还没有 GitHub 账号：
1. 访问 https://github.com
2. 点击 "Sign up" 注册
3. 填写用户名、邮箱、密码
4. 验证邮箱

### 第二步：创建新仓库

1. 登录 GitHub
2. 点击右上角的 "+" → "New repository"
3. 填写仓库信息：
   - Repository name: `your-username.github.io`（将 your-username 替换为您的用户名）
   - Description: 个人主页
   - 选择 "Public"
   - 勾选 "Add a README file"
4. 点击 "Create repository"

### 第三步：上传文件

**方法一：使用 Git 命令行**

```bash
# 进入项目目录
cd c:\Users\28162\Desktop\Personal_experience

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit: 个人主页"

# 添加远程仓库（替换为您的用户名）
git remote add origin https://github.com/your-username/your-username.github.io.git

# 推送到 GitHub
git push -u origin main
```

**方法二：使用 GitHub Desktop**

1. 下载并安装 GitHub Desktop: https://desktop.github.com
2. 打开 GitHub Desktop，登录您的账号
3. File → Add Local Repository → 选择项目文件夹
4. 点击 "Publish repository"
5. Repository name 填写 `your-username.github.io`
6. 点击 "Publish repository"

**方法三：网页上传**

1. 打开您创建的仓库页面
2. 点击 "Add file" → "Upload files"
3. 将所有文件拖拽到上传区域
4. 点击 "Commit changes"

### 第四步：启用 GitHub Pages

1. 进入仓库页面
2. 点击 "Settings"
3. 左侧菜单找到 "Pages"
4. Source 选择 "Deploy from a branch"
5. Branch 选择 "main"，文件夹选择 "/ (root)"
6. 点击 "Save"
7. 等待几分钟，页面会显示您的网站地址

### 第五步：访问您的网站

部署完成后，您的网站地址是：
```
https://your-username.github.io
```

---

## 🌐 其他部署选项

### Vercel（推荐备选）

1. 访问 https://vercel.com
2. 使用 GitHub 账号登录
3. 点击 "New Project"
4. 导入您的 GitHub 仓库
5. 点击 "Deploy"
6. 几分钟后获得免费域名

**优点：**
- 自动部署
- 更快的全球 CDN
- 自定义域名

### Netlify

1. 访问 https://www.netlify.com
2. 注册账号
3. 点击 "Add new site" → "Deploy manually"
4. 拖拽项目文件夹
5. 立即获得网站地址

---

## 📝 部署后注意事项

1. **更新内容**
   - 修改本地文件后，使用 `git add .` → `git commit -m "更新"` → `git push` 推送更新
   - GitHub Pages 会自动重新部署

2. **自定义域名**（可选）
   - 在 GitHub Pages 设置中添加自定义域名
   - 在域名服务商处配置 DNS

3. **SEO 优化**
   - 已包含基本的 meta 标签
   - 可添加 Google Analytics 追踪访问

---

## 🔧 快速命令

```bash
# 初始化并推送到 GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-username.github.io.git
git push -u origin main
```

---

## ❓ 常见问题

**Q: 为什么我的网站显示 404？**
A: 等待 5-10 分钟让 GitHub Pages 完成部署

**Q: 如何更新网站内容？**
A: 修改文件后执行 `git add .` → `git commit -m "更新"` → `git push`

**Q: 可以使用自定义域名吗？**
A: 可以，在 GitHub Pages 设置中添加自定义域名

**Q: 网站访问速度慢怎么办？**
A: 使用 Vercel 或 Netlify 部署，它们有全球 CDN 加速
