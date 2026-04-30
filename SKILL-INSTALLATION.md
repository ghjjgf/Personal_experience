# 个人主页生成器 Skill

## 📦 安装说明

### 方法一：手动安装

1. 将 `skills/personal-homepage-generator` 文件夹复制到您的 Trae skills 目录：
   ```
   C:\Users\<用户名>\.trae-cn\skills\
   ```

2. 完整路径应该是：
   ```
   C:\Users\<用户名>\.trae-cn\skills\personal-homepage-generator\SKILL.md
   ```

3. 重启 Trae 或刷新技能列表

### 方法二：使用命令

```powershell
# 创建目标目录
mkdir -p "$env:USERPROFILE\.trae-cn\skills\personal-homepage-generator"

# 复制skill文件
copy-item "skills\personal-homepage-generator\SKILL.md" "$env:USERPROFILE\.trae-cn\skills\personal-homepage-generator\"
```

---

## 🚀 使用方法

安装完成后，您可以在任何项目中使用这个skill：

### 示例对话

```
用户: 我想创建一个个人主页

助手: [自动调用 personal-homepage-generator skill]
好的！我来帮您创建个人主页。
您有PDF简历吗？如果有请提供路径...
```

---

## 📁 文件结构

```
Personal_experience/
├── tools/
│   └── homepage_generator.py    # 核心生成脚本
├── skills/
│   └── personal-homepage-generator/
│       └── SKILL.md             # Skill定义文件
└── SKILL-INSTALLATION.md        # 本文件
```

---

## 🔧 命令行使用

您也可以直接运行生成脚本：

```bash
# 交互式创建
python tools/homepage_generator.py --interactive

# 使用PDF简历
python tools/homepage_generator.py --pdf 简历.pdf

# 使用PDF和图片
python tools/homepage_generator.py --pdf 简历.pdf --images ./images

# 指定输出目录
python tools/homepage_generator.py --pdf 简历.pdf --output my-homepage
```

---

## ✨ 功能特点

1. **PDF解析**: 自动从PDF简历提取个人信息
2. **图片支持**: 支持项目截图和荣誉证书图片
3. **现代设计**: 暗黑科技风格，粒子背景
4. **响应式**: 适配桌面、平板、手机
5. **主题切换**: 支持深色/浅色模式
6. **易于部署**: 可直接部署到 GitHub Pages

---

## 📝 后续改进

- [ ] 更智能的PDF解析
- [ ] 更多主题模板
- [ ] 在线预览功能
- [ ] 一键部署集成
