# AI 图像生成指南

## 🎨 项目图片生成提示词

### 1. 智能除草机项目

**推荐工具：** DALL-E / Midjourney / Stable Diffusion

**提示词 (英文)：**
```
A modern agricultural smart weeding robot in rice field background, 
with camera and sensors on top, computer vision system detecting 
seedlings and weeds, futuristic tech style, high quality, 
professional product photography, blue and green color scheme
```

**提示词 (中文)：**
```
现代化的农业智能除草机器人，稻田背景，顶部带有摄像头和传感器，
计算机视觉系统识别秧苗和杂草，未来科技风格，高质量，
专业产品摄影，蓝绿色调
```

**建议尺寸：** 800x600 像素（横向）

---

### 2. 电能表时钟电池项目

**提示词 (英文)：**
```
Industrial smart electricity meter with lithium battery module, 
technical schematic overlay showing battery health monitoring, 
data visualization dashboard with charts and graphs, 
professional engineering documentation style, blue and white theme
```

**提示词 (中文)：**
```
工业智能电能表，带有锂电池模块，技术示意图显示电池健康监测，
数据可视化仪表板，包含图表和图形，
专业工程文档风格，蓝白主题
```

**建议尺寸：** 800x600 像素（横向）

---

### 3. 智慧工地安全监测平台

**提示词 (英文)：**
```
Construction site safety monitoring system with drone surveillance, 
AI camera detecting workers wearing hard hats and safety vests, 
real-time alert system interface, modern smart city technology, 
orange and blue color scheme, professional industrial photography
```

**提示词 (中文)：**
```
带有无人机监控的工地安全监测系统，AI摄像头识别工人安全帽和安全背心，
实时警报系统界面，现代智慧城市技术，
橙色和蓝色配色方案，专业工业摄影风格
```

**建议尺寸：** 800x600 像素（横向）

---

## 🚀 如何使用 AI 工具生成

### DALL-E (OpenAI)

1. 访问：https://chat.openai.com
2. 输入提示词
3. 选择生成图片
4. 下载并保存为 `.jpg` 格式

### Midjourney

1. 访问：https://www.midjourney.com
2. 在 Discord 中使用 `/imagine` 命令
3. 粘贴提示词
4. 下载并保存

### Stable Diffusion (本地部署)

1. 安装 Stable Diffusion
2. 在 Web UI 中粘贴提示词
3. 设置参数：
   - Steps: 30
   - CFG Scale: 7
   - Size: 800x600
4. 生成并保存

---

## 📁 保存图片到对应位置

生成后，将图片保存到以下位置：

```
assets/images/projects/
├── weeding-machine/
│   └── smart-weeding-robot.jpg    # 智能除草机
├── battery-system/
│   └── battery-monitoring.jpg     # 电池监测
└── safety-platform/
│   └── construction-monitoring.jpg # 安全监测
```

---

## 🔄 更新 HTML 引用

保存图片后，打开 `projects.html`，找到对应项目的图片区域，将：

```html
<div class="project-image" style="background: linear-gradient(...)"></div>
```

改为：

```html
<img class="project-image" src="assets/images/projects/weeding-machine/smart-weeding-robot.jpg" alt="智能除草机">
```

---

## 💡 提示词优化技巧

1. **添加风格关键词**：`professional`, `high quality`, `4k`, `detailed`
2. **指定颜色方案**：`blue and green theme`, `modern tech style`
3. **添加构图描述**：`product photography`, `technical illustration`, `dashboard UI`
4. **避免的内容**：`text`, `watermark`, `logo`

---

## 🎯 快速生成建议

如果您想快速获得结果，建议使用：

1. **DALL-E 3** (ChatGPT Plus) - 质量最高
2. **文心一格** (百度) - 中文支持好
3. **Stable Diffusion Online** - 免费

生成后告诉我文件路径，我可以帮您更新 HTML！
