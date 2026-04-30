---
name: "personal-homepage-generator"
description: "Generates a minimalist tech-style developer personal homepage from PDF resume and images. Invoke when user wants to create a personal portfolio website or asks about building a personal homepage."
---

# Personal Homepage Generator

A skill that generates a minimalist, high-end tech-style developer personal homepage from a PDF resume and images.

## When to Invoke

Invoke this skill when:
- User wants to create a personal portfolio website
- User asks about building a personal homepage
- User has a PDF resume and wants to convert it to a website
- User mentions "个人主页", "portfolio", "resume website"

## Features

- **PDF Resume Parsing**: Automatically extracts personal info, skills, projects from PDF
- **Image Integration**: Supports project screenshots and honor certificates
- **Modern Design**: Dark tech theme with particle background, smooth animations
- **Responsive**: Works on desktop, tablet, and mobile
- **Theme Toggle**: Dark/Light mode support
- **Easy Deployment**: Ready for GitHub Pages, Vercel, Netlify

## Usage

### Method 1: Interactive Mode

```
User: 我想创建一个个人主页
Assistant: [Invokes skill] 我来帮您创建个人主页...
```

### Method 2: With PDF Resume

```
User: 我有一个PDF简历，想转成网页
Assistant: [Invokes skill] 请提供PDF路径...
```

### Method 3: Full Setup

```
User: 帮我用这个PDF和图片创建个人主页
Assistant: [Invokes skill] 正在处理...
```

## Generated Structure

```
output/
├── index.html          # Homepage
├── projects.html       # Projects page
├── honors.html         # Honors page
├── css/
│   ├── themes.css      # Theme variables
│   ├── style.css       # Main styles
│   └── animations.css  # Animations
├── js/
│   ├── main.js         # Main logic
│   ├── particles.js    # Particle background
│   └── theme.js        # Theme toggle
├── assets/
│   └── images/
│       └── projects/
│           └── honors/ # Honor certificates
└── data.json           # Extracted data
```

## Implementation Steps

1. **Gather Information**
   - Ask for PDF resume (optional)
   - Ask for images directory (optional)
   - Collect personal info interactively if no PDF

2. **Extract Data**
   - Parse PDF for name, email, phone, skills, projects
   - Copy images to output directory

3. **Generate Website**
   - Create HTML files with extracted data
   - Generate CSS with theme variables
   - Generate JS for interactions

4. **Preview & Deploy**
   - Open local preview
   - Guide deployment to GitHub Pages/Vercel/Netlify

## Example Interaction

```
User: 我想创建一个个人主页，这是我的简历PDF

Assistant: 好的！我来帮您创建个人主页。

[Extracts info from PDF]
姓名: 张三
邮箱: zhangsan@example.com
...

[Generates website files]

✅ 个人主页生成完成！
📁 输出目录: output/
🌐 打开 output/index.html 查看效果

您满意吗？如果满意，我可以帮您部署到 GitHub Pages。
```

## Customization Options

- **Theme Colors**: Modify `css/themes.css`
- **Layout**: Adjust `css/style.css`
- **Content**: Edit HTML files or regenerate with new data
- **Images**: Replace in `assets/images/`

## Deployment

After generation, deploy using:
1. **GitHub Pages**: Push to `username.github.io` repo
2. **Vercel**: Connect GitHub repo or drag-drop
3. **Netlify**: Drag-drop output folder

## Requirements

- Python 3.6+
- PyPDF2 (auto-installed if missing)

## Notes

- PDF parsing is basic; manual verification recommended
- Images should be named meaningfully for best results
- The generated site uses no external dependencies (pure HTML/CSS/JS)
