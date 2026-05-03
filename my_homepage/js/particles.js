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