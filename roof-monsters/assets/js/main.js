/* =============================================
   Roof Monsters — main.js
   Hero slider (Ken Burns) · Mobile nav
   Testimonial carousel · CountUp · Form
============================================= */

document.addEventListener('DOMContentLoaded', () => {

  /* ── HERO SLIDER ───────────────────────── */
  const slides = document.querySelectorAll('.hero-slide');
  const dots   = document.querySelectorAll('.hero-dot');
  let current  = 0;
  let slideInterval;

  function goTo(index) {
    // Remove active + reset ken burns on outgoing slide
    const prevBg = slides[current].querySelector('.hero-slide-bg');
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    if (prevBg) {
      prevBg.style.animation = 'none';
      // Force reflow so animation resets next time
      void prevBg.offsetWidth;
    }

    current = (index + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current].classList.add('active');

    // Re-trigger ken burns on the newly active slide
    const newBg = slides[current].querySelector('.hero-slide-bg');
    if (newBg) {
      newBg.style.animation = 'none';
      void newBg.offsetWidth;
      newBg.style.animation = '';
    }
  }

  function startSlider() {
    slideInterval = setInterval(() => goTo(current + 1), 6000);
  }

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      clearInterval(slideInterval);
      goTo(i);
      startSlider();
    });
  });

  if (slides.length) startSlider();


  /* ── MOBILE NAV ────────────────────────── */
  const hamburger = document.getElementById('hamburger');
  const mainNav   = document.getElementById('mainNav');

  if (hamburger && mainNav) {
    hamburger.addEventListener('click', () => {
      mainNav.classList.toggle('open');
      hamburger.classList.toggle('active');
    });
  }


  /* ── TESTIMONIAL CAROUSEL ──────────────── */
  const track    = document.getElementById('testimonialTrack');
  const counter  = document.getElementById('tCounter');
  const prevBtn  = document.getElementById('tPrev');
  const nextBtn  = document.getElementById('tNext');

  if (track) {
    const cards     = track.querySelectorAll('.testimonial-card');
    let tCurrent    = 0;
    const total     = cards.length;

    function getPerView() {
      return window.innerWidth < 768 ? 1 : 3;
    }

    function updateCarousel() {
      const pv    = getPerView();
      const gap   = 28;
      const cardW = cards[0].offsetWidth;
      const shift = (cardW + gap) * tCurrent;
      track.style.transform = `translateX(-${shift}px)`;
      const maxIndex = Math.max(0, total - pv);
      if (counter) counter.textContent = `${tCurrent + 1} / ${Math.ceil(total / pv)}`;
      if (prevBtn) prevBtn.disabled = tCurrent === 0;
      if (nextBtn) nextBtn.disabled = tCurrent >= maxIndex;
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (tCurrent > 0) { tCurrent--; updateCarousel(); }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        const maxIndex = Math.max(0, total - getPerView());
        if (tCurrent < maxIndex) { tCurrent++; updateCarousel(); }
      });
    }

    window.addEventListener('resize', () => { tCurrent = 0; updateCarousel(); });
    updateCarousel();
  }


  /* ── COUNTUP ANIMATION ─────────────────── */
  function animateCountUp(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || ' +';
    const duration = 2000;   // ms
    const startTime = performance.now();

    function easeOutQuart(t) {
      return 1 - Math.pow(1 - t, 4);
    }

    function update(now) {
      const elapsed  = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased    = easeOutQuart(progress);
      const value    = Math.floor(eased * target);
      el.textContent = value.toLocaleString() + suffix;

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        el.textContent = target.toLocaleString() + suffix;
      }
    }

    requestAnimationFrame(update);
  }

  // Trigger countup when the stats section scrolls into view
  const statsSection = document.querySelector('[data-stats-section]');
  const statNums     = document.querySelectorAll('.stat-num[data-target]');
  let countupFired   = false;

  if (statsSection && statNums.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !countupFired) {
          countupFired = true;
          statNums.forEach(el => animateCountUp(el));
          observer.disconnect();
        }
      });
    }, { threshold: 0.3 });

    observer.observe(statsSection);
  }


  /* ── ESTIMATE FORM ─────────────────────── */
  const form = document.getElementById('estimateForm');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name  = form.querySelector('#fname').value.trim();
      const email = form.querySelector('#femail').value.trim();
      if (!name || !email) {
        alert('Please enter your name and email.');
        return;
      }
      alert(`Thank you, ${name}! We'll be in touch shortly.`);
      form.reset();
    });
  }


  /* ── ACTIVE NAV LINK ───────────────────── */
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.main-nav a').forEach(link => {
    if (link.getAttribute('href') === path) link.classList.add('active');
  });

});
