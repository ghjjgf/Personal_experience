import ParticleSystem from './particles.js';
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
});