// ===== Dark Mode Toggle =====
const themeToggle = document.getElementById('themeToggle');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const savedTheme = localStorage.getItem('theme');

// Set initial theme: saved preference > system preference > light
if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
  document.documentElement.setAttribute('data-theme', 'dark');
}

themeToggle.addEventListener('click', () => {
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  if (isDark) {
    document.documentElement.removeAttribute('data-theme');
    localStorage.setItem('theme', 'light');
    themeToggle.setAttribute('aria-label', 'Switch to dark mode');
  } else {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    themeToggle.setAttribute('aria-label', 'Switch to light mode');
  }
});

// ===== Mobile Navigation Toggle =====
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

navToggle.addEventListener('click', () => {
  navToggle.classList.toggle('active');
  navLinks.classList.toggle('active');
  const expanded = navToggle.getAttribute('aria-expanded') === 'true';
  navToggle.setAttribute('aria-expanded', String(!expanded));
  navToggle.setAttribute('aria-label', expanded ? 'Open menu' : 'Close menu');
});

// Close mobile menu when a link is clicked
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navToggle.classList.remove('active');
    navLinks.classList.remove('active');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.setAttribute('aria-label', 'Open menu');
  });
});

// ===== Scroll Animations =====
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

// Add fade-in class to elements that should animate
document.querySelectorAll(
  '.about-text, .highlight-card, .exp-card, .skill-category, .contact-card'
).forEach(el => {
  el.classList.add('fade-in');
  observer.observe(el);
});

// ===== Navbar background on scroll =====
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.style.boxShadow = '0 2px 12px rgba(0,0,0,0.08)';
  } else {
    navbar.style.boxShadow = 'none';
  }
});

// ===== Contact Form Validation =====
const contactForm = document.getElementById('contactForm');

if (contactForm) {
  const validators = {
    name: (v) => v.trim().length >= 2 ? '' : 'Please enter your name (at least 2 characters).',
    email: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : 'Please enter a valid email address.',
    message: (v) => v.trim().length >= 10 ? '' : 'Message must be at least 10 characters.',
  };

  function validateField(field) {
    const input = contactForm.elements[field];
    const error = document.getElementById(field + 'Error');
    const group = input.closest('.form-group');
    const msg = validators[field](input.value);
    if (error) error.textContent = msg;
    if (group) group.classList.toggle('error', !!msg);
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  }

  // Live validation on blur
  ['name', 'email', 'message'].forEach((field) => {
    const input = contactForm.elements[field];
    if (input) {
      input.addEventListener('blur', () => validateField(field));
      input.addEventListener('input', () => {
        const group = input.closest('.form-group');
        if (group && group.classList.contains('error')) validateField(field);
      });
    }
  });

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const fields = ['name', 'email', 'message'];
    const allValid = fields.every(validateField);

    if (allValid) {
      const btn = contactForm.querySelector('.btn-submit');
      const success = document.getElementById('formSuccess');
      btn.disabled = true;
      btn.textContent = 'Sending...';

      // Simulate submission (replace with actual endpoint)
      setTimeout(() => {
        btn.textContent = 'Sent!';
        success.hidden = false;
        contactForm.reset();

        setTimeout(() => {
          btn.disabled = false;
          btn.textContent = 'Send Message';
        }, 3000);
      }, 1000);
    }
  });
}
