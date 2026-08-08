(function () {
  'use strict';

  var header = document.getElementById('site-header');
  var navToggle = document.getElementById('nav-toggle');
  var navLinks = document.getElementById('nav-links');

  function onScroll() {
    if (header) {
      header.classList.toggle('scrolled', window.scrollY > 24);
    }
    var progress = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    header.style.setProperty('--scroll-progress', String(Math.min(progress, 1)));
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  function closeMenu() {
    if (navToggle && navToggle.getAttribute('aria-expanded') === 'true') {
      navToggle.setAttribute('aria-expanded', 'false');
      navLinks.classList.remove('is-open');
      document.body.style.overflow = '';
    }
  }

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var open = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!open));
      navLinks.classList.toggle('is-open', !open);
      document.body.style.overflow = open ? '' : 'hidden';
    });

    navLinks.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        closeMenu();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        closeMenu();
      }
    });
  }

  var sections = Array.prototype.slice.call(document.querySelectorAll('main section[id]'));
  var navAnchors = Array.prototype.slice.call(document.querySelectorAll('.nav-link'));

  var spy = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navAnchors.forEach(function (link) {
          link.classList.toggle('is-active', link.getAttribute('href') === '#' + entry.target.id);
        });
      });
    },
    { rootMargin: '-40% 0px -55% 0px' }
  );

  sections.forEach(function (section) {
    spy.observe(section);
  });

  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var reveal = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            reveal.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    revealEls.forEach(function (el) {
      reveal.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  var form = document.getElementById('contact-form');
  if (form) {
    var fields = {
      name: form.elements['name'],
      email: form.elements['email'],
      subject: form.elements['subject'],
      message: form.elements['message'],
    };

    function setError(field, message) {
      var err = field.parentElement.querySelector('.field-error');
      field.classList.add('is-invalid');
      if (err) {
        err.textContent = message;
        err.style.display = 'block';
      }
    }

    function clearError(field) {
      field.classList.remove('is-invalid');
      var err = field.parentElement.querySelector('.field-error');
      if (err) {
        err.textContent = '';
        err.style.display = 'none';
      }
    }

    function validateField(name) {
      var field = fields[name];
      var value = (field.value || '').trim();
      var valid = true;

      if (!value) {
        setError(field, 'This field is required.');
        valid = false;
      } else if (name === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value)) {
        setError(field, 'Please enter a valid email address.');
        valid = false;
      } else if (name === 'message' && value.length < 10) {
        setError(field, 'Message must be at least 10 characters long.');
        valid = false;
      } else if (name === 'name' && value.length < 2) {
        setError(field, 'Please enter your name.');
        valid = false;
      } else {
        clearError(field);
      }

      return valid;
    }

    Object.keys(fields).forEach(function (name) {
      fields[name].addEventListener('blur', function () {
        validateField(name);
      });
      fields[name].addEventListener('input', function () {
        if (fields[name].classList.contains('is-invalid')) {
          validateField(name);
        }
      });
    });

    form.addEventListener('submit', function (e) {
      var allValid = Object.keys(fields).every(validateField);
      if (!allValid) {
        e.preventDefault();
        var firstInvalid = form.querySelector('.is-invalid');
        if (firstInvalid) {
          firstInvalid.focus();
        }
      }
    });
  }

  if (new URLSearchParams(window.location.search).get('sent') === '1') {
    var target = document.getElementById('contact');
    if (target) {
      setTimeout(function () {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 150);
    }
  }
})();
