# 图片添加指南

## 📁 目录结构

```
assets/images/
├── avatar.jpg                    # 个人头像（300x300像素，正方形）
└── projects/
    ├── weeding-machine/          # 智能除草机项目图片
    │   ├── 除草机实习.jpg
    │   └── 除草机华为工程师.jpg
    ├── battery-system/           # 电能表时钟电池项目图片
    │   ├── 时钟电池实习.jpg
    │   ├── 时钟电池.jpg
    │   └── 时钟电池1.jpg
    ├── safety-platform/          # 智慧工地安全监测平台项目图片
    │   ├── safety-platform.jpg
    │   ├── 工地训练平台.jpg
    │   └── 工地软著.jpg
    └── honors/                   # 荣誉证书图片
        ├── 2024年"挑战杯"...jpg
        └── ...
```

---

## 🖼️ 如何添加新图片

### 方法一：直接添加图片文件

1. **将图片放入对应文件夹**
   - 智能除草机 → `assets/images/projects/weeding-machine/`
   - 电能表时钟电池 → `assets/images/projects/battery-system/`
   - 智慧工地安全监测平台 → `assets/images/projects/safety-platform/`
   - 荣誉证书 → `assets/images/projects/honors/`

2. **在 HTML 中添加图片标签**

   打开 `projects.html`，找到对应项目的图片区域，添加：

   ```html
   <div class="project-image-item">
     <img src="assets/images/projects/文件夹名/图片文件名.jpg" alt="图片描述" onclick="openModal(this.src)">
   </div>
   ```

### 方法二：使用配置文件（推荐）

1. **打开配置文件**
   ```
   js/project-config.js
   ```

2. **在对应项目中添加图片配置**
   ```javascript
   weedingMachine: {
     name: "智能除草机",
     folder: "weeding-machine",
     images: [
       { file: "除草机实习.jpg", alt: "除草机实习" },
       { file: "新图片.jpg", alt: "新图片描述" }  // 添加新图片
     ]
   }
   ```

---

## 📝 图片命名规范

- 使用有意义的名称，如：`除草机实习.jpg`、`工地训练平台.jpg`
- 支持中文命名
- 推荐格式：`.jpg`、`.png`、`.webp`
- 推荐尺寸：
  - 项目图片：800x600 像素（横向）
  - 荣誉证书：600x800 像素（纵向）

---

## 🎯 快速添加示例

### 添加新的项目图片

假设要为"智能除草机"项目添加一张新图片 `新照片.jpg`：

1. 将图片放入 `assets/images/projects/weeding-machine/` 文件夹

2. 打开 `projects.html`，找到智能除草机项目的图片区域，添加：

```html
<div class="project-images">
  <!-- 现有图片 -->
  <div class="project-image-item">
    <img src="assets/images/projects/weeding-machine/除草机实习.jpg" ...>
  </div>
  
  <!-- 新添加的图片 -->
  <div class="project-image-item">
    <img src="assets/images/projects/weeding-machine/新照片.jpg" alt="新照片描述" onclick="openModal(this.src)">
  </div>
</div>
```

### 添加新的荣誉证书

1. 将证书图片放入 `assets/images/projects/honors/` 文件夹

2. 打开 `projects.html`，找到荣誉证书区域，添加：

```html
<div class="honor-card">
  <img class="honor-image" src="assets/images/projects/honors/新证书.jpg" alt="新证书" onclick="openModal(this.src)">
  <div class="honor-content">
    <p class="honor-title">证书名称<br>获奖年份</p>
  </div>
</div>
```

---

## ⚠️ 注意事项

1. **图片大小**：建议单张图片不超过 2MB，以保证加载速度
2. **图片格式**：推荐使用 `.jpg` 格式（照片）或 `.png` 格式（证书）
3. **刷新页面**：添加图片后，刷新浏览器页面即可看到效果
4. **服务器运行**：确保本地服务器正在运行（`python -m http.server 8080`）

---

## 🔗 相关文件

- 项目页面：`projects.html`
- 图片配置：`js/project-config.js`
- 样式文件：`css/style.css`
