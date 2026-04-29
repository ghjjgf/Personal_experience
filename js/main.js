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
