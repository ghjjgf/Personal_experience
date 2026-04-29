# 极简科技风开发者个人主页实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建一个极简但高级感强的开发者个人主页，包含首页和项目页，支持深色/浅色主题切换和粒子动态背景。

**Architecture:** 采用原生 HTML/CSS/JavaScript 实现，无外部依赖。使用 CSS 变量管理主题，Canvas API 实现粒子背景，Intersection Observer API 实现滚动动画。页面结构清晰，文件职责单一。

**Tech Stack:** HTML5, CSS3 (CSS Variables, Flexbox, Grid), JavaScript ES6+ (Canvas API, Intersection Observer API, localStorage)

---

## 文件结构

```
personal-homepage/
├── index.html              # 首页
├── projects.html           # 项目页
├── css/
│   ├── themes.css          # 主题变量（深色/浅色）
│   ├── style.css           # 主样式（布局、组件）
│   └── animations.css      # 动画样式（关键帧、过渡）
├── js/
│   ├── utils.js            # 工具函数（节流、防抖等）
│   ├── particles.js        # 粒子背景系统
│   ├── theme.js            # 主题切换逻辑
│   └── main.js             # 主逻辑（导航、滚动、通用功能）
└── assets/
    ├── images/
    │   ├── avatar.jpg      # 头像（占位）
    │   └── projects/       # 项目截图目录
    └── icons/
        ├── github.svg      # GitHub 图标
        ├── linkedin.svg    # LinkedIn 图标
        ├── email.svg       # Email 图标
        └── blog.svg        # Blog 图标
```

---

## Task 1: 创建项目基础结构

**Files:**
- Create: `css/` (directory)
- Create: `js/` (directory)
- Create: `assets/images/` (directory)
- Create: `assets/images/projects/` (directory)
- Create: `assets/icons/` (directory)

- [ ] **Step 1: 创建目录结构**

```bash
mkdir -p css js assets/images/projects assets/icons
```

Expected: 目录创建成功

- [ ] **Step 2: 验证目录结构**

```bash
ls -la
```

Expected: 显示 css, js, assets 目录

---

## Task 2: 创建主题样式文件

**Files:**
- Create: `css/themes.css`

- [ ] **Step 1: 创建 themes.css 文件**

```css
:root {
  --color-bg-primary: #0a0a0f;
  --color-bg-secondary: #1a1a2e;
  --color-text-primary: #ffffff;
  --color-text-secondary: #a0a0a0;
  --color-accent: #00d4ff;
  --color-accent-secondary: #7c3aed;
  --gradient-primary: linear-gradient(135deg, #00d4ff 0%, #7c3aed 100%);
  
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 32px;
  --spacing-lg: 64px;
  --spacing-xl: 128px;
  
  --font-heading: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-code: 'JetBrains Mono', 'Fira Code', monospace;
  
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.6s ease;
  
  --shadow-sm: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 10px 20px rgba(0, 0, 0, 0.15);
  --shadow-lg: 0 20px 40px rgba(0, 212, 255, 0.3);
  
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 16px;
  
  --nav-height: 64px;
}

[data-theme="light"] {
  --color-bg-primary: #fafafa;
  --color-bg-secondary: #ffffff;
  --color-text-primary: #1a1a2e;
  --color-text-secondary: #6b7280;
  --color-accent: #0891b2;
  --color-accent-secondary: #6d28d9;
  --gradient-primary: linear-gradient(135deg, #0891b2 0%, #6d28d9 100%);
  
  --shadow-sm: 0 4px 6px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 10px 20px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 20px 40px rgba(8, 145, 178, 0.2);
}
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la css/
```

Expected: 显示 themes.css 文件

---

## Task 3: 创建主样式文件

**Files:**
- Create: `css/style.css`

- [ ] **Step 1: 创建 style.css - 基础样式**

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-body);
  background-color: var(--color-bg-primary);
  color: var(--color-text-primary);
  line-height: 1.6;
  overflow-x: hidden;
  transition: background-color var(--transition-normal), color var(--transition-normal);
}

a {
  color: inherit;
  text-decoration: none;
  transition: color var(--transition-fast);
}

a:hover {
  color: var(--color-accent);
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
}

ul, ol {
  list-style: none;
}
```

- [ ] **Step 2: 添加导航栏样式**

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: var(--nav-height);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 var(--spacing-lg);
  z-index: 1000;
  background: transparent;
  transition: background-color var(--transition-normal), backdrop-filter var(--transition-normal);
}

.nav.scrolled {
  background: rgba(10, 10, 15, 0.9);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

[data-theme="light"] .nav.scrolled {
  background: rgba(250, 250, 250, 0.9);
}

.nav-logo {
  font-size: 1.5rem;
  font-weight: 700;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

.nav-link {
  position: relative;
  padding: var(--spacing-xs) 0;
  font-weight: 500;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--gradient-primary);
  transition: width var(--transition-normal);
}

.nav-link:hover::after,
.nav-link.active::after {
  width: 100%;
}

.theme-toggle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-primary);
  transition: all var(--transition-fast);
}

.theme-toggle:hover {
  color: var(--color-accent);
  transform: scale(1.1);
}

.theme-toggle svg {
  width: 20px;
  height: 20px;
}
```

- [ ] **Step 3: 添加 Hero 区域样式**

```css
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-xl) var(--spacing-lg);
  text-align: center;
}

.hero-content {
  position: relative;
  z-index: 1;
}

.hero-avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: var(--spacing-md);
  border: 3px solid transparent;
  background: var(--gradient-primary) border-box;
  transition: transform var(--transition-normal), box-shadow var(--transition-normal);
}

.hero-avatar:hover {
  transform: scale(1.05);
  box-shadow: 0 0 30px rgba(0, 212, 255, 0.4);
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: var(--spacing-xs);
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.5rem;
  color: var(--color-text-secondary);
  margin-bottom: var(--spacing-sm);
}

.hero-description {
  font-size: 1.125rem;
  color: var(--color-text-secondary);
  max-width: 600px;
  margin-bottom: var(--spacing-md);
}

.hero-social {
  display: flex;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-lg);
}

.social-link {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--color-text-secondary);
  color: var(--color-text-secondary);
  transition: all var(--transition-fast);
}

.social-link:hover {
  color: var(--color-accent);
  border-color: var(--color-accent);
  transform: scale(1.1);
}

.social-link svg {
  width: 24px;
  height: 24px;
}

.scroll-indicator {
  position: absolute;
  bottom: var(--spacing-lg);
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-xs);
  color: var(--color-text-secondary);
  animation: bounce 2s infinite;
}

.scroll-indicator svg {
  width: 24px;
  height: 24px;
}
```

- [ ] **Step 4: 添加项目区域样式**

```css
.section {
  padding: var(--spacing-xl) var(--spacing-lg);
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: var(--spacing-md);
  position: relative;
  display: inline-block;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 60px;
  height: 3px;
  background: var(--gradient-primary);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-md);
  margin-top: var(--spacing-lg);
}

.project-card {
  background: var(--color-bg-secondary);
  border-radius: var(--border-radius-md);
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all var(--transition-normal);
}

[data-theme="light"] .project-card {
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.project-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-lg);
  border-color: rgba(0, 212, 255, 0.5);
}

.project-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  background: var(--color-bg-primary);
}

.project-content {
  padding: var(--spacing-md);
}

.project-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: var(--spacing-xs);
}

.project-description {
  color: var(--color-text-secondary);
  font-size: 0.9rem;
  margin-bottom: var(--spacing-sm);
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-xs);
  margin-bottom: var(--spacing-sm);
}

.project-tag {
  padding: 4px 12px;
  background: rgba(0, 212, 255, 0.1);
  border-radius: var(--border-radius-sm);
  font-size: 0.8rem;
  font-family: var(--font-code);
  color: var(--color-accent);
  transition: all var(--transition-fast);
}

.project-tag:hover {
  background: rgba(0, 212, 255, 0.2);
}

.project-link {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-xs);
  color: var(--color-accent);
  font-weight: 500;
  transition: gap var(--transition-fast);
}

.project-link:hover {
  gap: var(--spacing-sm);
}
```

- [ ] **Step 5: 添加技能区域样式**

```css
.skills-section {
  padding: var(--spacing-xl) var(--spacing-lg);
  max-width: 1200px;
  margin: 0 auto;
}

.skills-category {
  margin-bottom: var(--spacing-lg);
}

.skills-category-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: var(--spacing-md);
  color: var(--color-text-secondary);
}

.skills-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-sm);
}

.skill-tag {
  padding: var(--spacing-xs) var(--spacing-md);
  background: var(--color-bg-secondary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--border-radius-md);
  font-family: var(--font-code);
  font-size: 0.9rem;
  transition: all var(--transition-fast);
}

[data-theme="light"] .skill-tag {
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.skill-tag:hover {
  color: var(--color-accent);
  border-color: var(--color-accent);
  transform: scale(1.05);
}
```

- [ ] **Step 6: 添加联系区域样式**

```css
.contact-section {
  padding: var(--spacing-xl) var(--spacing-lg);
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.contact-description {
  font-size: 1.125rem;
  color: var(--color-text-secondary);
  margin-bottom: var(--spacing-lg);
}

.contact-links {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
  align-items: center;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  background: var(--color-bg-secondary);
  border-radius: var(--border-radius-md);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all var(--transition-fast);
  min-width: 300px;
}

[data-theme="light"] .contact-link {
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.contact-link:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
}

.contact-link svg {
  width: 20px;
  height: 20px;
}
```

- [ ] **Step 7: 添加响应式样式**

```css
@media (max-width: 768px) {
  .nav {
    padding: 0 var(--spacing-md);
  }
  
  .nav-links {
    gap: var(--spacing-sm);
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.25rem;
  }
  
  .hero-avatar {
    width: 120px;
    height: 120px;
  }
  
  .section {
    padding: var(--spacing-lg) var(--spacing-md);
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    font-size: 1.5rem;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

- [ ] **Step 8: 验证文件创建**

```bash
ls -la css/
```

Expected: 显示 style.css 文件

---

## Task 4: 创建动画样式文件

**Files:**
- Create: `css/animations.css`

- [ ] **Step 1: 创建 animations.css 文件**

```css
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateX(-50%) translateY(0);
  }
  40% {
    transform: translateX(-50%) translateY(-10px);
  }
  60% {
    transform: translateX(-50%) translateY(-5px);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
}

.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
}

.animate-scale-in {
  animation: scaleIn 0.3s ease-out forwards;
}

.scroll-animate {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.scroll-animate.visible {
  opacity: 1;
  transform: translateY(0);
}

.stagger-1 { transition-delay: 0.1s; }
.stagger-2 { transition-delay: 0.2s; }
.stagger-3 { transition-delay: 0.3s; }
.stagger-4 { transition-delay: 0.4s; }
.stagger-5 { transition-delay: 0.5s; }
.stagger-6 { transition-delay: 0.6s; }

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  
  .scroll-animate {
    opacity: 1;
    transform: none;
  }
}
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la css/
```

Expected: 显示 animations.css 文件

---

## Task 5: 创建工具函数文件

**Files:**
- Create: `js/utils.js`

- [ ] **Step 1: 创建 utils.js 文件**

```javascript
const throttle = (func, limit) => {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
};

const debounce = (func, wait) => {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
};

const lerp = (start, end, factor) => {
  return start + (end - start) * factor;
};

const clamp = (value, min, max) => {
  return Math.min(Math.max(value, min), max);
};

const randomRange = (min, max) => {
  return Math.random() * (max - min) + min;
};

const getDeviceType = () => {
  const width = window.innerWidth;
  if (width < 768) return 'mobile';
  if (width < 1024) return 'tablet';
  return 'desktop';
};

const getParticleCount = () => {
  const deviceType = getDeviceType();
  switch (deviceType) {
    case 'mobile':
      return 30;
    case 'tablet':
      return 75;
    default:
      return 120;
  }
};

const isReducedMotion = () => {
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
};

const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    console.error('Failed to copy:', err);
    return false;
  }
};

export {
  throttle,
  debounce,
  lerp,
  clamp,
  randomRange,
  getDeviceType,
  getParticleCount,
  isReducedMotion,
  copyToClipboard
};
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la js/
```

Expected: 显示 utils.js 文件

---

## Task 6: 创建粒子背景系统

**Files:**
- Create: `js/particles.js`

- [ ] **Step 1: 创建 particles.js 文件**

```javascript
import { throttle, randomRange, getParticleCount, isReducedMotion } from './utils.js';

class Particle {
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.x = options.x || randomRange(0, canvas.width);
    this.y = options.y || randomRange(0, canvas.height);
    this.size = options.size || randomRange(1, 3);
    this.speedX = randomRange(-0.5, 0.5);
    this.speedY = randomRange(-0.5, 0.5);
    this.color = options.color || 'rgba(0, 212, 255, 0.8)';
  }

  update(mouse) {
    this.x += this.speedX;
    this.y += this.speedY;

    if (this.x < 0 || this.x > this.canvas.width) this.speedX *= -1;
    if (this.y < 0 || this.y > this.canvas.height) this.speedY *= -1;

    if (mouse.x !== null && mouse.y !== null) {
      const dx = mouse.x - this.x;
      const dy = mouse.y - this.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      
      if (distance < 150) {
        const force = (150 - distance) / 150;
        this.x -= dx * force * 0.02;
        this.y -= dy * force * 0.02;
      }
    }
  }

  draw() {
    this.ctx.beginPath();
    this.ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    this.ctx.fillStyle = this.color;
    this.ctx.fill();
  }
}

class ParticleSystem {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    
    this.ctx = this.canvas.getContext('2d');
    this.particles = [];
    this.mouse = { x: null, y: null };
    this.animationId = null;
    this.isVisible = true;
    
    this.colors = {
      dark: 'rgba(0, 212, 255, 0.8)',
      light: 'rgba(8, 145, 178, 0.8)'
    };
    
    this.init();
  }

  init() {
    this.resize();
    this.createParticles();
    this.bindEvents();
    if (!isReducedMotion()) {
      this.animate();
    } else {
      this.drawStatic();
    }
  }

  resize() {
    const dpr = window.devicePixelRatio || 1;
    const rect = this.canvas.getBoundingClientRect();
    
    this.canvas.width = rect.width * dpr;
    this.canvas.height = rect.height * dpr;
    this.ctx.scale(dpr, dpr);
    
    this.canvas.style.width = rect.width + 'px';
    this.canvas.style.height = rect.height + 'px';
  }

  createParticles() {
    const count = getParticleCount();
    const theme = document.documentElement.getAttribute('data-theme') || 'dark';
    const color = this.colors[theme];
    
    this.particles = [];
    for (let i = 0; i < count; i++) {
      this.particles.push(new Particle(this.canvas, { color }));
    }
  }

  updateParticleColors() {
    const theme = document.documentElement.getAttribute('data-theme') || 'dark';
    const color = this.colors[theme];
    
    this.particles.forEach(particle => {
      particle.color = color;
    });
  }

  bindEvents() {
    window.addEventListener('resize', throttle(() => {
      this.resize();
      this.createParticles();
    }, 200));

    this.canvas.addEventListener('mousemove', throttle((e) => {
      const rect = this.canvas.getBoundingClientRect();
      this.mouse.x = e.clientX - rect.left;
      this.mouse.y = e.clientY - rect.top;
    }, 16));

    this.canvas.addEventListener('mouseleave', () => {
      this.mouse.x = null;
      this.mouse.y = null;
    });

    document.addEventListener('visibilitychange', () => {
      this.isVisible = !document.hidden;
      if (this.isVisible && !isReducedMotion()) {
        this.animate();
      }
    });
  }

  drawConnections() {
    const maxDistance = 120;
    
    for (let i = 0; i < this.particles.length; i++) {
      for (let j = i + 1; j < this.particles.length; j++) {
        const dx = this.particles[i].x - this.particles[j].x;
        const dy = this.particles[i].y - this.particles[j].y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        
        if (distance < maxDistance) {
          const opacity = (1 - distance / maxDistance) * 0.3;
          this.ctx.beginPath();
          this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
          this.ctx.lineTo(this.particles[j].x, this.particles[j].y);
          this.ctx.strokeStyle = `rgba(0, 212, 255, ${opacity})`;
          this.ctx.lineWidth = 0.5;
          this.ctx.stroke();
        }
      }
    }
  }

  animate() {
    if (!this.isVisible) return;
    
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    this.particles.forEach(particle => {
      particle.update(this.mouse);
      particle.draw();
    });
    
    this.drawConnections();
    
    this.animationId = requestAnimationFrame(() => this.animate());
  }

  drawStatic() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    this.particles.forEach(particle => {
      particle.draw();
    });
    
    this.drawConnections();
  }

  destroy() {
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
    }
  }
}

export default ParticleSystem;
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la js/
```

Expected: 显示 particles.js 文件

---

## Task 7: 创建主题切换逻辑

**Files:**
- Create: `js/theme.js`

- [ ] **Step 1: 创建 theme.js 文件**

```javascript
class ThemeManager {
  constructor() {
    this.theme = this.getStoredTheme() || this.getPreferredTheme();
    this.init();
  }

  getStoredTheme() {
    return localStorage.getItem('theme');
  }

  getPreferredTheme() {
    return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }

  setTheme(theme) {
    this.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    const event = new CustomEvent('themechange', { detail: { theme } });
    document.dispatchEvent(event);
  }

  toggle() {
    const newTheme = this.theme === 'dark' ? 'light' : 'dark';
    this.setTheme(newTheme);
  }

  init() {
    this.setTheme(this.theme);
    
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!localStorage.getItem('theme')) {
        this.setTheme(e.matches ? 'dark' : 'light');
      }
    });
  }
}

const themeManager = new ThemeManager();

export default themeManager;
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la js/
```

Expected: 显示 theme.js 文件

---

## Task 8: 创建主逻辑文件

**Files:**
- Create: `js/main.js`

- [ ] **Step 1: 创建 main.js 文件**

```javascript
import ParticleSystem from './particles.js';
import themeManager from './theme.js';
import { throttle } from './utils.js';

class App {
  constructor() {
    this.nav = document.querySelector('.nav');
    this.themeToggle = document.querySelector('.theme-toggle');
    this.particleSystem = null;
    
    this.init();
  }

  init() {
    this.initParticles();
    this.initNavigation();
    this.initScrollAnimations();
    this.initThemeToggle();
    this.initSmoothScroll();
  }

  initParticles() {
    const canvas = document.getElementById('particles-canvas');
    if (canvas) {
      this.particleSystem = new ParticleSystem('particles-canvas');
      
      document.addEventListener('themechange', () => {
        if (this.particleSystem) {
          this.particleSystem.updateParticleColors();
        }
      });
    }
  }

  initNavigation() {
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', throttle(() => {
      const currentScrollY = window.scrollY;
      
      if (currentScrollY > 50) {
        this.nav.classList.add('scrolled');
      } else {
        this.nav.classList.remove('scrolled');
      }
      
      lastScrollY = currentScrollY;
    }, 16));
  }

  initScrollAnimations() {
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.2
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.querySelectorAll('.scroll-animate').forEach(el => {
      observer.observe(el);
    });
  }

  initThemeToggle() {
    if (this.themeToggle) {
      this.updateThemeIcon();
      
      this.themeToggle.addEventListener('click', () => {
        themeManager.toggle();
        this.updateThemeIcon();
      });
      
      document.addEventListener('themechange', () => {
        this.updateThemeIcon();
      });
    }
  }

  updateThemeIcon() {
    const sunIcon = this.themeToggle.querySelector('.sun-icon');
    const moonIcon = this.themeToggle.querySelector('.moon-icon');
    
    if (themeManager.theme === 'dark') {
      sunIcon.style.display = 'block';
      moonIcon.style.display = 'none';
    } else {
      sunIcon.style.display = 'none';
      moonIcon.style.display = 'block';
    }
  }

  initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new App();
});
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la js/
```

Expected: 显示 main.js 文件

---

## Task 9: 创建首页 HTML

**Files:**
- Create: `index.html`

- [ ] **Step 1: 创建 index.html 文件**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="极简科技风开发者个人主页 - 展示项目作品、技能结构和联系方式">
  <meta name="keywords" content="开发者, 个人主页, 前端, 后端, 全栈">
  <meta property="og:title" content="开发者个人主页">
  <meta property="og:description" content="极简科技风开发者个人主页">
  <meta property="og:type" content="website">
  <title>开发者个人主页</title>
  <link rel="stylesheet" href="css/themes.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/animations.css">
</head>
<body>
  <canvas id="particles-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;"></canvas>

  <nav class="nav">
    <a href="index.html" class="nav-logo">Dev</a>
    <div class="nav-links">
      <a href="index.html" class="nav-link active">首页</a>
      <a href="projects.html" class="nav-link">项目</a>
      <button class="theme-toggle" aria-label="切换主题">
        <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
        <svg class="moon-icon" style="display: none;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      </button>
    </div>
  </nav>

  <section class="hero">
    <div class="hero-content">
      <img src="assets/images/avatar.jpg" alt="头像" class="hero-avatar scroll-animate">
      <h1 class="hero-title scroll-animate stagger-1">开发者姓名</h1>
      <p class="hero-subtitle scroll-animate stagger-2">全栈开发者 / 技术爱好者</p>
      <p class="hero-description scroll-animate stagger-3">
        热爱技术，专注于构建优雅、高效的数字产品。擅长前端开发与后端架构，追求代码的艺术与工程的完美结合。
      </p>
      <div class="hero-social scroll-animate stagger-4">
        <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="GitHub">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
        </a>
        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="LinkedIn">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
          </svg>
        </a>
        <a href="mailto:email@example.com" class="social-link" aria-label="Email">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2h-16c-1.1 0-2-.9-2-2v-12c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
          </svg>
        </a>
      </div>
    </div>
    <div class="scroll-indicator">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="6 9 12 15 18 9"></polyline>
      </svg>
    </div>
  </section>

  <section class="section" id="projects">
    <h2 class="section-title scroll-animate">精选项目</h2>
    <div class="projects-grid">
      <div class="project-card scroll-animate stagger-1">
        <div class="project-image" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">项目名称 1</h3>
          <p class="project-description">这是一个使用现代技术栈构建的全栈应用，展示了前后端分离架构的最佳实践。</p>
          <div class="project-tags">
            <span class="project-tag">React</span>
            <span class="project-tag">Node.js</span>
            <span class="project-tag">MongoDB</span>
          </div>
          <a href="projects.html" class="project-link">
            查看详情
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </a>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-2">
        <div class="project-image" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">项目名称 2</h3>
          <p class="project-description">一个高性能的数据可视化平台，支持实时数据流处理和交互式图表展示。</p>
          <div class="project-tags">
            <span class="project-tag">Vue</span>
            <span class="project-tag">D3.js</span>
            <span class="project-tag">WebSocket</span>
          </div>
          <a href="projects.html" class="project-link">
            查看详情
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </a>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-3">
        <div class="project-image" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">项目名称 3</h3>
          <p class="project-description">开源命令行工具，提升开发效率，支持多平台和插件扩展机制。</p>
          <div class="project-tags">
            <span class="project-tag">Go</span>
            <span class="project-tag">CLI</span>
            <span class="project-tag">开源</span>
          </div>
          <a href="projects.html" class="project-link">
            查看详情
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </a>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-4">
        <div class="project-image" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">项目名称 4</h3>
          <p class="project-description">微服务架构的电商平台，包含用户管理、订单系统、支付网关等核心模块。</p>
          <div class="project-tags">
            <span class="project-tag">微服务</span>
            <span class="project-tag">Docker</span>
            <span class="project-tag">K8s</span>
          </div>
          <a href="projects.html" class="project-link">
            查看详情
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </a>
        </div>
      </div>
    </div>
    <div style="text-align: center; margin-top: var(--spacing-lg);">
      <a href="projects.html" class="project-link" style="font-size: 1.125rem;">
        查看所有项目
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </a>
    </div>
  </section>

  <section class="skills-section" id="skills">
    <h2 class="section-title scroll-animate">技能栈</h2>
    
    <div class="skills-category scroll-animate stagger-1">
      <h3 class="skills-category-title">前端开发</h3>
      <div class="skills-tags">
        <span class="skill-tag">HTML5</span>
        <span class="skill-tag">CSS3</span>
        <span class="skill-tag">JavaScript</span>
        <span class="skill-tag">TypeScript</span>
        <span class="skill-tag">React</span>
        <span class="skill-tag">Vue</span>
        <span class="skill-tag">Next.js</span>
      </div>
    </div>

    <div class="skills-category scroll-animate stagger-2">
      <h3 class="skills-category-title">后端开发</h3>
      <div class="skills-tags">
        <span class="skill-tag">Node.js</span>
        <span class="skill-tag">Python</span>
        <span class="skill-tag">Go</span>
        <span class="skill-tag">Java</span>
        <span class="skill-tag">PostgreSQL</span>
        <span class="skill-tag">MongoDB</span>
        <span class="skill-tag">Redis</span>
      </div>
    </div>

    <div class="skills-category scroll-animate stagger-3">
      <h3 class="skills-category-title">工具 & 其他</h3>
      <div class="skills-tags">
        <span class="skill-tag">Git</span>
        <span class="skill-tag">Docker</span>
        <span class="skill-tag">Kubernetes</span>
        <span class="skill-tag">AWS</span>
        <span class="skill-tag">CI/CD</span>
        <span class="skill-tag">Linux</span>
      </div>
    </div>
  </section>

  <section class="contact-section" id="contact">
    <h2 class="section-title scroll-animate">联系我</h2>
    <p class="contact-description scroll-animate stagger-1">
      有项目想法或合作机会？欢迎随时联系我。
    </p>
    <div class="contact-links scroll-animate stagger-2">
      <a href="mailto:email@example.com" class="contact-link">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2h-16c-1.1 0-2-.9-2-2v-12c0-1.1.9-2 2-2z"></path>
          <polyline points="22,6 12,13 2,6"></polyline>
        </svg>
        email@example.com
      </a>
      <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="contact-link">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
        GitHub
      </a>
      <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="contact-link">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
        </svg>
        LinkedIn
      </a>
    </div>
  </section>

  <footer style="text-align: center; padding: var(--spacing-lg); color: var(--color-text-secondary); border-top: 1px solid rgba(255, 255, 255, 0.1);">
    <p>&copy; 2024 开发者姓名. All rights reserved.</p>
  </footer>

  <script type="module" src="js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la
```

Expected: 显示 index.html 文件

---

## Task 10: 创建项目页 HTML

**Files:**
- Create: `projects.html`

- [ ] **Step 1: 创建 projects.html 文件**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="项目作品展示 - 查看我的所有项目作品">
  <title>项目作品 - 开发者个人主页</title>
  <link rel="stylesheet" href="css/themes.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/animations.css">
  <style>
    .projects-header {
      position: relative;
      min-height: 50vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: var(--spacing-xl) var(--spacing-lg);
    }
    
    .filter-bar {
      display: flex;
      justify-content: center;
      gap: var(--spacing-sm);
      flex-wrap: wrap;
      margin-bottom: var(--spacing-lg);
    }
    
    .filter-btn {
      padding: var(--spacing-xs) var(--spacing-md);
      background: transparent;
      border: 1px solid var(--color-text-secondary);
      border-radius: var(--border-radius-md);
      color: var(--color-text-secondary);
      font-family: inherit;
      cursor: pointer;
      transition: all var(--transition-fast);
    }
    
    .filter-btn:hover,
    .filter-btn.active {
      color: var(--color-accent);
      border-color: var(--color-accent);
    }
    
    .projects-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 var(--spacing-lg) var(--spacing-xl);
    }
    
    .no-projects {
      text-align: center;
      padding: var(--spacing-xl);
      color: var(--color-text-secondary);
    }
  </style>
</head>
<body>
  <canvas id="particles-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;"></canvas>

  <nav class="nav">
    <a href="index.html" class="nav-logo">Dev</a>
    <div class="nav-links">
      <a href="index.html" class="nav-link">首页</a>
      <a href="projects.html" class="nav-link active">项目</a>
      <button class="theme-toggle" aria-label="切换主题">
        <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
        <svg class="moon-icon" style="display: none;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      </button>
    </div>
  </nav>

  <section class="projects-header">
    <h1 class="hero-title scroll-animate">我的项目</h1>
    <p class="hero-subtitle scroll-animate stagger-1">探索我的作品与技术实践</p>
    <div class="scroll-indicator">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="6 9 12 15 18 9"></polyline>
      </svg>
    </div>
  </section>

  <section class="projects-container">
    <div class="filter-bar scroll-animate">
      <button class="filter-btn active" data-filter="all">全部</button>
      <button class="filter-btn" data-filter="frontend">前端</button>
      <button class="filter-btn" data-filter="backend">后端</button>
      <button class="filter-btn" data-filter="fullstack">全栈</button>
      <button class="filter-btn" data-filter="tool">工具</button>
    </div>

    <div class="projects-grid" id="projects-grid">
      <div class="project-card scroll-animate stagger-1" data-type="fullstack">
        <div class="project-image" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">全栈电商平台</h3>
          <p class="project-description">这是一个使用现代技术栈构建的全栈应用，展示了前后端分离架构的最佳实践。包含用户认证、商品管理、购物车、订单系统等核心功能。</p>
          <div class="project-tags">
            <span class="project-tag">React</span>
            <span class="project-tag">Node.js</span>
            <span class="project-tag">MongoDB</span>
          </div>
          <div style="display: flex; gap: var(--spacing-sm);">
            <a href="#" class="project-link">查看详情</a>
            <a href="#" class="project-link">源代码</a>
          </div>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-2" data-type="frontend">
        <div class="project-image" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">数据可视化平台</h3>
          <p class="project-description">一个高性能的数据可视化平台，支持实时数据流处理和交互式图表展示。包含多种图表类型和自定义主题功能。</p>
          <div class="project-tags">
            <span class="project-tag">Vue</span>
            <span class="project-tag">D3.js</span>
            <span class="project-tag">WebSocket</span>
          </div>
          <div style="display: flex; gap: var(--spacing-sm);">
            <a href="#" class="project-link">查看详情</a>
            <a href="#" class="project-link">源代码</a>
          </div>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-3" data-type="tool">
        <div class="project-image" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">CLI 开发工具</h3>
          <p class="project-description">开源命令行工具，提升开发效率，支持多平台和插件扩展机制。包含项目脚手架、代码生成、自动化部署等功能。</p>
          <div class="project-tags">
            <span class="project-tag">Go</span>
            <span class="project-tag">CLI</span>
            <span class="project-tag">开源</span>
          </div>
          <div style="display: flex; gap: var(--spacing-sm);">
            <a href="#" class="project-link">查看详情</a>
            <a href="#" class="project-link">源代码</a>
          </div>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-4" data-type="backend">
        <div class="project-image" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">微服务架构系统</h3>
          <p class="project-description">微服务架构的电商平台后端，包含用户管理、订单系统、支付网关等核心模块。支持高并发和水平扩展。</p>
          <div class="project-tags">
            <span class="project-tag">微服务</span>
            <span class="project-tag">Docker</span>
            <span class="project-tag">K8s</span>
          </div>
          <div style="display: flex; gap: var(--spacing-sm);">
            <a href="#" class="project-link">查看详情</a>
            <a href="#" class="project-link">源代码</a>
          </div>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-5" data-type="frontend">
        <div class="project-image" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">移动端 UI 组件库</h3>
          <p class="project-description">一套高质量的移动端 UI 组件库，包含 30+ 常用组件，支持主题定制和按需加载。</p>
          <div class="project-tags">
            <span class="project-tag">React</span>
            <span class="project-tag">TypeScript</span>
            <span class="project-tag">移动端</span>
          </div>
          <div style="display: flex; gap: var(--spacing-sm);">
            <a href="#" class="project-link">查看详情</a>
            <a href="#" class="project-link">源代码</a>
          </div>
        </div>
      </div>

      <div class="project-card scroll-animate stagger-6" data-type="fullstack">
        <div class="project-image" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);"></div>
        <div class="project-content">
          <h3 class="project-title">在线协作工具</h3>
          <p class="project-description">实时协作的在线文档编辑工具，支持多人同时编辑、评论、版本控制等功能。</p>
          <div class="project-tags">
            <span class="project-tag">Next.js</span>
            <span class="project-tag">WebSocket</span>
            <span class="project-tag">CRDT</span>
          </div>
          <div style="display: flex; gap: var(--spacing-sm);">
            <a href="#" class="project-link">查看详情</a>
            <a href="#" class="project-link">源代码</a>
          </div>
        </div>
      </div>
    </div>

    <div class="no-projects" id="no-projects" style="display: none;">
      <p>暂无此类项目</p>
    </div>
  </section>

  <footer style="text-align: center; padding: var(--spacing-lg); color: var(--color-text-secondary); border-top: 1px solid rgba(255, 255, 255, 0.1);">
    <a href="index.html" style="display: inline-flex; align-items: center; gap: var(--spacing-xs); margin-bottom: var(--spacing-sm);">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="15 18 9 12 15 6"></polyline>
      </svg>
      返回首页
    </a>
    <p>&copy; 2024 开发者姓名. All rights reserved.</p>
  </footer>

  <script type="module" src="js/main.js"></script>
  <script type="module">
    import { throttle } from './js/utils.js';
    
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const noProjects = document.getElementById('no-projects');
    
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        const filter = btn.dataset.filter;
        let visibleCount = 0;
        
        projectCards.forEach(card => {
          if (filter === 'all' || card.dataset.type === filter) {
            card.style.display = 'block';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        });
        
        noProjects.style.display = visibleCount === 0 ? 'block' : 'none';
      });
    });
  </script>
</body>
</html>
```

- [ ] **Step 2: 验证文件创建**

```bash
ls -la
```

Expected: 显示 projects.html 文件

---

## Task 11: 创建占位资源文件

**Files:**
- Create: `assets/images/avatar.jpg` (占位图片)
- Create: `assets/icons/github.svg`
- Create: `assets/icons/linkedin.svg`
- Create: `assets/icons/email.svg`
- Create: `assets/icons/blog.svg`

- [ ] **Step 1: 创建占位头像说明文件**

```bash
echo "请将您的头像图片放置于此，命名为 avatar.jpg" > assets/images/README.txt
```

Expected: 创建说明文件

- [ ] **Step 2: 创建 GitHub 图标 SVG**

```xml
<svg viewBox="0 0 24 24" fill="currentColor">
  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
</svg>
```

- [ ] **Step 3: 创建 LinkedIn 图标 SVG**

```xml
<svg viewBox="0 0 24 24" fill="currentColor">
  <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
</svg>
```

- [ ] **Step 4: 创建 Email 图标 SVG**

```xml
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2h-16c-1.1 0-2-.9-2-2v-12c0-1.1.9-2 2-2z"></path>
  <polyline points="22,6 12,13 2,6"></polyline>
</svg>
```

- [ ] **Step 5: 创建 Blog 图标 SVG**

```xml
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
  <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
</svg>
```

- [ ] **Step 6: 验证文件创建**

```bash
ls -la assets/icons/
```

Expected: 显示所有图标文件

---

## Task 12: 最终验证与测试

**Files:**
- Verify: All files created correctly

- [ ] **Step 1: 验证所有文件结构**

```bash
find . -type f -name "*.html" -o -name "*.css" -o -name "*.js" | head -20
```

Expected: 显示所有创建的文件

- [ ] **Step 2: 在浏览器中打开首页测试**

```bash
# 如果有本地服务器，启动它
# 或者直接在浏览器中打开 index.html
```

Expected: 页面正常显示，粒子背景运行，主题切换正常

- [ ] **Step 3: 测试响应式布局**

在浏览器开发者工具中测试不同设备尺寸：
- 移动端 (< 768px)
- 平板 (768px - 1024px)
- 桌面 (> 1024px)

Expected: 布局正确响应

- [ ] **Step 4: 测试主题切换**

点击主题切换按钮，验证：
- 深色/浅色主题切换
- 颜色正确变化
- localStorage 保存偏好

Expected: 主题切换正常工作

- [ ] **Step 5: 测试滚动动画**

滚动页面，验证：
- 元素渐入动画
- 导航栏背景变化
- 粒子背景持续运行

Expected: 动画流畅

- [ ] **Step 6: 测试项目筛选（项目页）**

打开 projects.html，测试项目筛选功能：
- 点击不同筛选按钮
- 项目正确过滤
- 无结果提示显示

Expected: 筛选功能正常

---

## 实现完成

完成以上所有任务后，项目应该具备以下功能：

1. ✅ 首页：Hero 区域、精选项目、技能展示、联系方式
2. ✅ 项目页：项目网格、筛选功能
3. ✅ 粒子背景系统
4. ✅ 主题切换（深色/浅色）
5. ✅ 滚动动画
6. ✅ 响应式布局
7. ✅ 无外部依赖（纯原生实现）

**后续优化建议：**
- 添加真实的项目截图和内容
- 优化粒子背景性能（根据实际设备调整）
- 添加更多交互细节
- SEO 优化（添加 sitemap.xml、robots.txt）
- 添加 Google Analytics 或其他分析工具
