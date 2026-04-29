const projectImages = {
  weedingMachine: {
    name: "智能除草机",
    folder: "weeding-machine",
    images: [
      { file: "除草机实习.jpg", alt: "除草机实习" },
      { file: "除草机华为工程师.jpg", alt: "除草机华为工程师" }
    ]
  },
  batterySystem: {
    name: "电能表时钟电池",
    folder: "battery-system",
    images: [
      { file: "时钟电池实习.jpg", alt: "时钟电池实习" },
      { file: "时钟电池.jpg", alt: "时钟电池" },
      { file: "时钟电池1.jpg", alt: "时钟电池1" }
    ]
  },
  safetyPlatform: {
    name: "智慧工地安全监测平台",
    folder: "safety-platform",
    images: [
      { file: "safety-platform.jpg", alt: "安全监测平台" },
      { file: "工地训练平台.jpg", alt: "工地训练平台" },
      { file: "工地软著.jpg", alt: "软件著作权" }
    ]
  },
  honors: {
    name: "荣誉证书",
    folder: "honors",
    images: [
      { file: "2024年"挑战杯"大学生创业计划竞赛校级特等奖.jpg", alt: "挑战杯特等奖", title: "2024年"挑战杯"大学生创业计划竞赛<br>校级特等奖" },
      { file: "数学建模国赛.jpg", alt: "数学建模", title: "2024年全国大学生数学建模<br>省级三等奖" },
      { file: "人工智能大赛省级三等奖.png", alt: "人工智能大赛", title: "2025年中国机器人及人工智能大赛<br>省级三等奖" },
      { file: "发明专利1公开证明2025.11.14.jpg", alt: "发明专利1", title: "发明专利公开证明 (一)<br>2025年" },
      { file: "发明专利2公开证明2025.9.9.jpg", alt: "发明专利2", title: "发明专利公开证明 (二)<br>2025年" },
      { file: "奖学金2.jpg", alt: "奖学金", title: "学业奖学金<br>2024-2026年" },
      { file: "2024-2025年度第二学期校级三等奖学金.jpg", alt: "三等奖学金", title: "2024-2025年度第二学期<br>校级三等奖学金" },
      { file: "优秀共青团员证书.jpg", alt: "优秀共青团员", title: "优秀共青团员<br>2025年" }
    ]
  }
};

function getImagePath(projectKey, imageIndex) {
  const project = projectImages[projectKey];
  if (!project) return null;
  const image = project.images[imageIndex];
  if (!image) return null;
  return `assets/images/projects/${project.folder}/${image.file}`;
}

function getAllProjectImages(projectKey) {
  const project = projectImages[projectKey];
  if (!project) return [];
  return project.images.map((img, index) => ({
    src: `assets/images/projects/${project.folder}/${img.file}`,
    alt: img.alt,
    title: img.title || null
  }));
}

export { projectImages, getImagePath, getAllProjectImages };
