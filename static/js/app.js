gsap.from('.hero h1', { opacity: 0, y: 30, duration: 1, ease: 'power3.out' });

gsap.from('.hero p', { opacity: 0, y: 20, duration: 0.9, delay: 0.2 });

gsap.from('.hero .btn-primary', { opacity: 0, y: 20, duration: 0.8, delay: 0.4 });

gsap.from('.hero .btn-secondary', { opacity: 0, y: 20, duration: 0.8, delay: 0.5 });

ScrollReveal().reveal('.feature-card', {
  distance: '40px',
  duration: 900,
  interval: 120,
  origin: 'bottom',
});

ScrollReveal().reveal('.glass-card', {
  distance: '30px',
  duration: 800,
  origin: 'bottom',
  interval: 100,
});
