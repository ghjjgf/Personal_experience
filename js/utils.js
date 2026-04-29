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
