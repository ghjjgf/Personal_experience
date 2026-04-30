#!/usr/bin/env python3
"""
个人主页生成器
通过上传PDF简历和图片，自动生成极简科技风开发者个人主页
"""

import os
import sys
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime

try:
    import PyPDF2
except ImportError:
    print("正在安装 PyPDF2...")
    os.system("pip install PyPDF2 -q")
    import PyPDF2

class PersonalHomepageGenerator:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.template_dir = Path(__file__).parent
        self.data = {
            "name": "开发者",
            "title": "后端开发工程师",
            "university": "",
            "email": "",
            "phone": "",
            "description": "",
            "skills": {},
            "projects": [],
            "honors": []
        }
    
    def extract_from_pdf(self, pdf_path):
        """从PDF简历中提取信息"""
        print(f"📖 正在读取PDF: {pdf_path}")
        
        try:
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            
            print("✅ PDF读取成功！")
            print("\n" + "="*50)
            print("提取的文本内容：")
            print("="*50)
            print(text[:2000] + "..." if len(text) > 2000 else text)
            print("="*50 + "\n")
            
            return text
        except Exception as e:
            print(f"❌ 读取PDF失败: {e}")
            return None
    
    def parse_resume_text(self, text):
        """解析简历文本，提取关键信息"""
        import re
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            if not line:
                continue
            
            if '姓名' in line or '姓 名' in line:
                parts = re.split(r'[：:]', line)
                if len(parts) > 1:
                    self.data['name'] = parts[1].strip()
            
            if '邮箱' in line or '邮 箱' in line or '@' in line:
                emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', line)
                if emails:
                    self.data['email'] = emails[0]
            
            if '电话' in line or '联系' in line:
                phones = re.findall(r'1[3-9]\d{9}', line)
                if phones:
                    self.data['phone'] = phones[0]
            
            if '毕业院校' in line or '大学' in line or '学院' in line:
                if '毕业院校' in line:
                    parts = re.split(r'[：:]', line)
                    if len(parts) > 1:
                        self.data['university'] = parts[1].strip()
                elif not self.data['university']:
                    self.data['university'] = line
        
        self._parse_skills(text)
        self._parse_projects(text)
        self._parse_honors(text)
        
        return self.data
    
    def _parse_skills(self, text):
        """解析技能部分"""
        import re
        
        skill_keywords = {
            '编程语言': ['C', 'C\\+\\+', 'Python', 'Java', 'JavaScript', 'Go', 'Rust', 'TypeScript'],
            '后端开发': ['Linux', 'IO多路复用', 'epoll', 'select', 'poll', 'Qt', 'OpenVINO'],
            '深度学习': ['YOLO', 'BPNN', '计算机视觉', '模型训练', '端侧部署'],
            '工具': ['Git', 'Docker', 'MySQL', 'Redis', 'MongoDB']
        }
        
        found_skills = {cat: [] for cat in skill_keywords}
        
        for category, keywords in skill_keywords.items():
            for keyword in keywords:
                if re.search(keyword, text, re.IGNORECASE):
                    skill_name = keyword.replace('\\+', '+')
                    if skill_name not in found_skills[category]:
                        found_skills[category].append(skill_name)
        
        for category, skills in found_skills.items():
            if skills:
                self.data['skills'][category] = skills
    
    def _parse_projects(self, text):
        """解析项目部分"""
        import re
        
        project_pattern = r'(\d{4}年\d{1,2}月[—\-至]+\d{4}年\d{1,2}月)\s+(.+?)\s+(后端开发工程师|核心成员|负责人)'
        
        projects = []
        seen_names = set()
        
        matches = re.findall(project_pattern, text)
        for match in matches:
            if len(match) >= 3:
                project_name = match[1].strip()
                if project_name not in seen_names and len(project_name) > 2:
                    project = {
                        "name": project_name,
                        "time": match[0].strip(),
                        "role": match[2].strip(),
                        "description": "",
                        "tech": [],
                        "results": ""
                    }
                    projects.append(project)
                    seen_names.add(project_name)
        
        tech_matches = re.findall(r'技术栈[：:]\s*([^。\n]+)', text)
        for i, tech_str in enumerate(tech_matches):
            if i < len(projects):
                tech_list = [t.strip() for t in re.split(r'[、，,]', tech_str) if t.strip()]
                projects[i]['tech'] = tech_list
        
        self.data['projects'] = projects[:5]
    
    def _parse_honors(self, text):
        """解析荣誉部分"""
        import re
        
        honors = []
        seen_honors = set()
        
        honor_patterns = [
            r'(\d{4}年[^,\n，]{3,30}(?:一等奖|二等奖|三等奖|特等奖|优秀奖))',
            r'(挑战杯[^,\n，]{0,20}(?:特等奖|一等奖|二等奖|三等奖)?)',
            r'(数学建模[^,\n，]{0,20}(?:一等奖|二等奖|三等奖)?)',
            r'(发明专利[^,\n，]{0,30})',
            r'(优秀[^,\n，]{2,8}(?:证书)?)',
            r'(人工智能大赛[^,\n，]{0,20}(?:一等奖|二等奖|三等奖)?)'
        ]
        
        for pattern in honor_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                honor_name = match.strip()
                if honor_name and len(honor_name) > 4 and honor_name not in seen_honors:
                    honors.append({
                        "name": honor_name,
                        "date": "",
                        "image": ""
                    })
                    seen_honors.add(honor_name)
        
        years = re.findall(r'(\d{4})年', text)
        for i, honor in enumerate(honors):
            if i < len(years):
                honor["date"] = years[i] + "年"
        
        self.data['honors'] = honors[:10]
    
    def interactive_input(self):
        """交互式输入个人信息"""
        print("\n" + "="*50)
        print("📝 请输入个人信息（直接回车跳过）")
        print("="*50 + "\n")
        
        self.data['name'] = input(f"姓名 [{self.data['name']}]: ").strip() or self.data['name']
        self.data['title'] = input(f"职位 [{self.data['title']}]: ").strip() or self.data['title']
        self.data['university'] = input(f"学校 [{self.data['university']}]: ").strip() or self.data['university']
        self.data['email'] = input(f"邮箱 [{self.data['email']}]: ").strip() or self.data['email']
        self.data['phone'] = input(f"电话 [{self.data['phone']}]: ").strip() or self.data['phone']
        self.data['description'] = input("个人简介: ").strip() or "热爱技术，专注于构建优雅、高效的数字产品。"
        
        print("\n" + "-"*50)
        print("技能输入（输入空行结束）")
        print("-"*50)
        
        categories = ["编程语言", "后端开发", "前端开发", "工具", "其他"]
        for category in categories:
            skills_input = input(f"{category}技能（用逗号分隔）: ").strip()
            if skills_input:
                self.data['skills'][category] = [s.strip() for s in skills_input.split(',')]
        
        print("\n" + "-"*50)
        print("项目输入（输入空行结束）")
        print("-"*50)
        
        while True:
            project_name = input("项目名称（空行结束）: ").strip()
            if not project_name:
                break
            
            project = {
                "name": project_name,
                "description": input("项目描述: ").strip(),
                "tech": input("技术栈（用逗号分隔）: ").strip().split(','),
                "time": input("项目时间: ").strip(),
                "role": input("担任角色: ").strip(),
                "results": input("项目成果: ").strip()
            }
            self.data['projects'].append(project)
        
        print("\n" + "-"*50)
        print("荣誉输入（输入空行结束）")
        print("-"*50)
        
        while True:
            honor_name = input("荣誉名称（空行结束）: ").strip()
            if not honor_name:
                break
            
            honor = {
                "name": honor_name,
                "date": input("获奖时间: ").strip()
            }
            self.data['honors'].append(honor)
    
    def copy_images(self, images_dir):
        """复制图片到输出目录并自动匹配荣誉"""
        images_path = Path(images_dir)
        if not images_path.exists():
            print(f"⚠️ 图片目录不存在: {images_dir}")
            return
        
        output_images = self.output_dir / "assets" / "images"
        output_projects = output_images / "projects"
        output_honors = output_projects / "honors"
        
        output_honors.mkdir(parents=True, exist_ok=True)
        
        copied_images = []
        for img in images_path.glob("*"):
            if img.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                dest = output_honors / img.name
                shutil.copy(img, dest)
                copied_images.append(img.name)
                print(f"📷 复制图片: {img.name}")
        
        self._match_honor_images(copied_images)
    
    def _match_honor_images(self, images):
        """自动匹配荣誉图片"""
        import re
        
        for honor in self.data['honors']:
            honor_name = honor.get('name', '')
            
            for img in images:
                img_lower = img.lower()
                
                if '挑战杯' in honor_name and '挑战杯' in img_lower:
                    honor['image'] = img
                    break
                elif '数学建模' in honor_name and '数学建模' in img_lower:
                    honor['image'] = img
                    break
                elif '专利' in honor_name and '专利' in img_lower:
                    honor['image'] = img
                    break
                elif '优秀' in honor_name and '优秀' in img_lower:
                    honor['image'] = img
                    break
                elif '奖学金' in honor_name and '奖学金' in img_lower:
                    honor['image'] = img
                    break
                elif '人工智能' in honor_name and '人工智能' in img_lower:
                    honor['image'] = img
                    break
        
        for i, honor in enumerate(self.data['honors']):
            if not honor.get('image') and i < len(images):
                honor['image'] = images[i]
    
    def generate_html(self):
        """生成HTML文件"""
        print("\n🔧 正在生成HTML文件...")
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        dirs = [
            self.output_dir / "css",
            self.output_dir / "js",
            self.output_dir / "assets" / "images" / "projects" / "honors"
        ]
        
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
        
        self._generate_index_html()
        self._generate_projects_html()
        self._generate_honors_html()
        self._generate_css()
        self._generate_js()
        
        print("✅ HTML文件生成完成！")
    
    def _generate_index_html(self):
        """生成首页HTML"""
        skills_html = ""
        for category, skills in self.data['skills'].items():
            skills_html += f'''
            <div class="skills-category scroll-animate">
              <h3 class="skills-category-title">{category}</h3>
              <div class="skills-tags">
                {''.join([f'<span class="skill-tag">{s}</span>' for s in skills])}
              </div>
            </div>'''
        
        projects_html = ""
        for i, project in enumerate(self.data['projects'][:3], 1):
            projects_html += f'''
          <div class="project-card scroll-animate stagger-{i}">
            <img class="project-image" src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&h=600&fit=crop" alt="{project['name']}" style="width: 100%; height: 200px; object-fit: cover;">
            <div class="project-content">
              <h3 class="project-title">{project['name']}</h3>
              <p class="project-description">{project['description']}</p>
              <div class="project-tags">
                {''.join([f'<span class="project-tag">{t.strip()}</span>' for t in project['tech']])}
              </div>
              <a href="projects.html" class="project-link">查看详情</a>
            </div>
          </div>'''
        
        honors_html = ""
        for honor in self.data['honors'][:6]:
            honors_html += f'''
          <div class="honor-badge">
            <span class="honor-icon">🏆</span>
            <span class="honor-text">{honor['name']}</span>
          </div>'''
        
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{self.data['name']} - {self.data['title']}</title>
  <link rel="stylesheet" href="css/themes.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/animations.css">
</head>
<body>
  <canvas id="particles-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;"></canvas>

  <nav class="nav">
    <a href="index.html" class="nav-logo">{self.data['name']}</a>
    <div class="nav-links">
      <a href="index.html" class="nav-link active">首页</a>
      <a href="projects.html" class="nav-link">项目</a>
      <a href="honors.html" class="nav-link">荣誉</a>
      <a href="#contact" class="nav-link">联系</a>
      <button class="theme-toggle" aria-label="切换主题">
        <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
        </svg>
        <svg class="moon-icon" style="display: none;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      </button>
    </div>
  </nav>

  <section class="hero">
    <div class="hero-content">
      <h1 class="hero-title scroll-animate">{self.data['name']}</h1>
      <p class="hero-subtitle scroll-animate stagger-1">{self.data['title']} / {self.data['university']}</p>
      <p class="hero-description scroll-animate stagger-2">{self.data['description']}</p>
      <div class="hero-social scroll-animate stagger-3">
        <a href="mailto:{self.data['email']}" class="social-link">📧</a>
      </div>
    </div>
  </section>

  <section class="section" id="projects">
    <h2 class="section-title scroll-animate">精选项目</h2>
    <div class="projects-grid">{projects_html}
    </div>
  </section>

  <section class="skills-section" id="skills">
    <h2 class="section-title scroll-animate">专业技能</h2>{skills_html}
  </section>

  <section class="section" id="honors">
    <h2 class="section-title scroll-animate">荣誉证书</h2>
    <div class="honors-preview">{honors_html}
    </div>
    <div style="text-align: center; margin-top: var(--spacing-md);">
      <a href="honors.html" class="project-link">查看所有荣誉证书</a>
    </div>
  </section>

  <section class="contact-section" id="contact">
    <h2 class="section-title scroll-animate">联系我</h2>
    <div class="contact-links scroll-animate">
      <a href="mailto:{self.data['email']}" class="contact-link">📧 {self.data['email']}</a>
      <a href="tel:{self.data['phone']}" class="contact-link">📱 {self.data['phone']}</a>
    </div>
  </section>

  <footer style="text-align: center; padding: var(--spacing-lg); color: var(--color-text-secondary);">
    <p>&copy; {datetime.now().year} {self.data['name']}. All rights reserved.</p>
  </footer>

  <script type="module" src="js/main.js"></script>
</body>
</html>'''
        
        with open(self.output_dir / "index.html", 'w', encoding='utf-8') as f:
            f.write(html)
    
    def _generate_projects_html(self):
        """生成项目页HTML"""
        projects_html = ""
        for i, project in enumerate(self.data['projects'], 1):
            projects_html += f'''
      <div class="project-detail-card scroll-animate">
        <div class="project-header">
          <div class="project-meta">
            <span>📅 {project['time']}</span>
            <span class="project-role">{project['role']}</span>
          </div>
          <h2 class="project-title-large">{project['name']}</h2>
          <div class="project-tech-stack">
            {''.join([f'<span class="project-tag">{t.strip()}</span>' for t in project['tech']])}
          </div>
        </div>
        <div class="project-body">
          <div class="project-section">
            <h3 class="project-section-title">项目描述</h3>
            <p class="project-section-content">{project['description']}</p>
          </div>
          <div class="project-section">
            <h3 class="project-section-title">项目成果</h3>
            <div class="project-result-box">
              <p>{project['results']}</p>
            </div>
          </div>
        </div>
      </div>'''
        
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>项目作品 - {self.data['name']}</title>
  <link rel="stylesheet" href="css/themes.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/animations.css">
</head>
<body>
  <canvas id="particles-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;"></canvas>

  <nav class="nav">
    <a href="index.html" class="nav-logo">{self.data['name']}</a>
    <div class="nav-links">
      <a href="index.html" class="nav-link">首页</a>
      <a href="projects.html" class="nav-link active">项目</a>
      <a href="honors.html" class="nav-link">荣誉</a>
      <a href="index.html#contact" class="nav-link">联系</a>
    </div>
  </nav>

  <section class="projects-header">
    <h1 class="hero-title scroll-animate">我的项目</h1>
    <p class="hero-subtitle scroll-animate stagger-1">探索我的作品与技术实践</p>
  </section>

  <section class="projects-container">{projects_html}
  </section>

  <footer style="text-align: center; padding: var(--spacing-lg); color: var(--color-text-secondary);">
    <a href="index.html">← 返回首页</a>
    <p>&copy; {datetime.now().year} {self.data['name']}. All rights reserved.</p>
  </footer>

  <script type="module" src="js/main.js"></script>
</body>
</html>'''
        
        with open(self.output_dir / "projects.html", 'w', encoding='utf-8') as f:
            f.write(html)
    
    def _generate_honors_html(self):
        """生成荣誉页HTML"""
        honors_html = ""
        for i, honor in enumerate(self.data['honors'], 1):
            honors_html += f'''
    <div class="honor-card scroll-animate stagger-{i % 8}">
      <div class="honor-image-container">
        <img class="honor-image" src="assets/images/projects/honors/{honor.get('image', 'default.jpg')}" alt="{honor['name']}">
      </div>
      <div class="honor-content">
        <h3 class="honor-title">{honor['name']}</h3>
        <p class="honor-date">{honor['date']}</p>
      </div>
    </div>'''
        
        html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>荣誉证书 - {self.data['name']}</title>
  <link rel="stylesheet" href="css/themes.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/animations.css">
</head>
<body>
  <canvas id="particles-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;"></canvas>

  <nav class="nav">
    <a href="index.html" class="nav-logo">{self.data['name']}</a>
    <div class="nav-links">
      <a href="index.html" class="nav-link">首页</a>
      <a href="projects.html" class="nav-link">项目</a>
      <a href="honors.html" class="nav-link active">荣誉</a>
      <a href="index.html#contact" class="nav-link">联系</a>
    </div>
  </nav>

  <section class="honors-header">
    <h1 class="hero-title scroll-animate">荣誉证书</h1>
    <p class="hero-subtitle scroll-animate stagger-1">点击图片查看大图</p>
  </section>

  <section class="honors-grid">{honors_html}
  </section>

  <footer style="text-align: center; padding: var(--spacing-lg); color: var(--color-text-secondary);">
    <a href="index.html">← 返回首页</a>
    <p>&copy; {datetime.now().year} {self.data['name']}. All rights reserved.</p>
  </footer>

  <script type="module" src="js/main.js"></script>
</body>
</html>'''
        
        with open(self.output_dir / "honors.html", 'w', encoding='utf-8') as f:
            f.write(html)
    
    def _generate_css(self):
        """生成CSS文件"""
        css_themes = ''':root {
  --color-bg-primary: #0a0a0f;
  --color-bg-secondary: #1a1a2e;
  --color-text-primary: #ffffff;
  --color-text-secondary: #a0a0a0;
  --color-accent: #00d4ff;
  --gradient-primary: linear-gradient(135deg, #00d4ff 0%, #7c3aed 100%);
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 32px;
  --spacing-lg: 64px;
  --spacing-xl: 128px;
  --font-heading: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-code: 'JetBrains Mono', monospace;
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
  --shadow-lg: 0 20px 40px rgba(0, 212, 255, 0.3);
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --nav-height: 64px;
}

[data-theme="light"] {
  --color-bg-primary: #fafafa;
  --color-bg-secondary: #ffffff;
  --color-text-primary: #1a1a2e;
  --color-text-secondary: #6b7280;
  --color-accent: #0891b2;
}'''
        
        with open(self.output_dir / "css" / "themes.css", 'w', encoding='utf-8') as f:
            f.write(css_themes)
        
        css_style = '''@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

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

.contact-section {
  padding: var(--spacing-xl) var(--spacing-lg);
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
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

.honors-preview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--spacing-sm);
}

.honor-badge {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  background: var(--color-bg-secondary);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--border-radius-md);
  transition: all var(--transition-fast);
}

[data-theme="light"] .honor-badge {
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.honor-badge:hover {
  border-color: var(--color-accent);
  transform: translateX(4px);
}

.honor-icon {
  font-size: 1.25rem;
  flex-shrink: 0;
}

.honor-text {
  font-size: 0.9rem;
  color: var(--color-text-secondary);
  line-height: 1.4;
}

.projects-header, .honors-header {
  padding: calc(var(--spacing-xl) + var(--nav-height)) var(--spacing-lg) var(--spacing-lg);
  text-align: center;
}

.projects-container {
  padding: 0 var(--spacing-lg) var(--spacing-xl);
  max-width: 900px;
  margin: 0 auto;
}

.project-detail-card {
  background: var(--color-bg-secondary);
  border-radius: var(--border-radius-md);
  margin-bottom: var(--spacing-lg);
  border: 1px solid rgba(255, 255, 255, 0.1);
  overflow: hidden;
}

[data-theme="light"] .project-detail-card {
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.project-header {
  padding: var(--spacing-md);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

[data-theme="light"] .project-header {
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.project-meta {
  display: flex;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-xs);
  color: var(--color-text-secondary);
  font-size: 0.9rem;
}

.project-role {
  color: var(--color-accent);
}

.project-title-large {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: var(--spacing-sm);
}

.project-tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-xs);
}

.project-body {
  padding: var(--spacing-md);
}

.project-section {
  margin-bottom: var(--spacing-md);
}

.project-section-title {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: var(--spacing-xs);
  color: var(--color-text-secondary);
}

.project-section-content {
  color: var(--color-text-primary);
  line-height: 1.8;
}

.project-result-box {
  background: rgba(0, 212, 255, 0.1);
  padding: var(--spacing-md);
  border-radius: var(--border-radius-md);
  border-left: 3px solid var(--color-accent);
}

.honors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--spacing-md);
  padding: 0 var(--spacing-lg) var(--spacing-xl);
  max-width: 1200px;
  margin: 0 auto;
}

.honor-card {
  background: var(--color-bg-secondary);
  border-radius: var(--border-radius-md);
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all var(--transition-normal);
}

[data-theme="light"] .honor-card {
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.honor-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.honor-image-container {
  width: 100%;
  height: 200px;
  overflow: hidden;
  background: var(--color-bg-primary);
}

.honor-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-normal);
}

.honor-card:hover .honor-image {
  transform: scale(1.05);
}

.honor-content {
  padding: var(--spacing-sm);
}

.honor-title {
  font-size: 0.95rem;
  font-weight: 500;
  margin-bottom: var(--spacing-xs);
}

.honor-date {
  font-size: 0.8rem;
  color: var(--color-text-secondary);
}

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
}'''
        
        with open(self.output_dir / "css" / "style.css", 'w', encoding='utf-8') as f:
            f.write(css_style)
        
        css_animations = '''@keyframes bounce {
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
.stagger-7 { transition-delay: 0.7s; }
.stagger-8 { transition-delay: 0.8s; }

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
}'''
        
        with open(self.output_dir / "css" / "animations.css", 'w', encoding='utf-8') as f:
            f.write(css_animations)
        
        print("✅ CSS文件生成完成")
    
    def _generate_js(self):
        """生成JS文件"""
        js_utils = '''export function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

export function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

export function randomRange(min, max) {
  return Math.random() * (max - min) + min;
}

export function getParticleCount() {
  const width = window.innerWidth;
  if (width < 768) return 30;
  if (width < 1200) return 50;
  return 80;
}

export function isReducedMotion() {
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}'''
        
        with open(self.output_dir / "js" / "utils.js", 'w', encoding='utf-8') as f:
            f.write(js_utils)
        
        js_theme = '''class ThemeManager {
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

export default themeManager;'''
        
        with open(self.output_dir / "js" / "theme.js", 'w', encoding='utf-8') as f:
            f.write(js_theme)
        
        js_particles = '''import { throttle, randomRange, getParticleCount, isReducedMotion } from './utils.js';

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

export default ParticleSystem;'''
        
        with open(self.output_dir / "js" / "particles.js", 'w', encoding='utf-8') as f:
            f.write(js_particles)
        
        js_main = '''import ParticleSystem from './particles.js';
import themeManager from './theme.js';

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
  }

  initParticles() {
    const canvas = document.getElementById('particles-canvas');
    if (canvas) {
      this.particleSystem = new ParticleSystem('particles-canvas');
    }
  }

  initNavigation() {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        this.nav.classList.add('scrolled');
      } else {
        this.nav.classList.remove('scrolled');
      }
    });
  }

  initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.2 });

    document.querySelectorAll('.scroll-animate').forEach(el => {
      observer.observe(el);
    });
  }

  initThemeToggle() {
    if (this.themeToggle) {
      this.themeToggle.addEventListener('click', () => {
        themeManager.toggle();
      });
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new App();
});'''
        
        with open(self.output_dir / "js" / "main.js", 'w', encoding='utf-8') as f:
            f.write(js_main)
        
        print("✅ JS文件生成完成")
    
    def save_data(self):
        """保存数据到JSON文件"""
        with open(self.output_dir / "data.json", 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print(f"✅ 数据已保存到 {self.output_dir / 'data.json'}")


def main():
    parser = argparse.ArgumentParser(description='个人主页生成器')
    parser.add_argument('--pdf', help='PDF简历路径')
    parser.add_argument('--images', help='图片目录路径')
    parser.add_argument('--output', default='output', help='输出目录')
    parser.add_argument('--interactive', action='store_true', help='交互式输入')
    
    args = parser.parse_args()
    
    generator = PersonalHomepageGenerator(output_dir=args.output)
    
    if args.pdf:
        text = generator.extract_from_pdf(args.pdf)
        if text:
            generator.parse_resume_text(text)
    
    if args.interactive or not args.pdf:
        generator.interactive_input()
    
    if args.images:
        generator.copy_images(args.images)
    
    generator.generate_html()
    generator.save_data()
    
    print("\n" + "="*50)
    print("🎉 个人主页生成完成！")
    print("="*50)
    print(f"📁 输出目录: {args.output}")
    print(f"🌐 打开 {args.output}/index.html 查看效果")
    print("="*50)


if __name__ == "__main__":
    main()
