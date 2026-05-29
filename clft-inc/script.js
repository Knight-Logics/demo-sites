// ---- Current year ----
const currentYear = document.querySelector("#current-year");
if (currentYear) {
  currentYear.textContent = new Date().getFullYear();
}

// ---- Scroll reveal ----
const revealItems = document.querySelectorAll("[data-reveal]");
if ("IntersectionObserver" in window && revealItems.length > 0) {
  const observer = new IntersectionObserver(
    (entries, activeObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        activeObserver.unobserve(entry.target);
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -40px 0px" }
  );
  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

// ---- Demo contact form (shows success state without real submission) ----
const heroForm    = document.getElementById("hero-contact-form");
const formSuccess = document.getElementById("form-success");

if (heroForm && formSuccess) {
  heroForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const submitBtn = heroForm.querySelector("[type='submit']");
    submitBtn.disabled = true;
    submitBtn.textContent = "Sending...";
    setTimeout(() => {
      heroForm.hidden = true;
      formSuccess.hidden = false;
    }, 900);
  });
}

// ---- Hamburger menu ----
const hamburgerBtn = document.getElementById("hamburger-btn");
const mobileNav    = document.getElementById("mobile-nav");

if (hamburgerBtn && mobileNav) {
  hamburgerBtn.addEventListener("click", () => {
    const expanded = hamburgerBtn.getAttribute("aria-expanded") === "true";
    hamburgerBtn.setAttribute("aria-expanded", String(!expanded));
    mobileNav.classList.toggle("is-open");
  });

  // Close on mobile nav link click
  mobileNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      hamburgerBtn.setAttribute("aria-expanded", "false");
      mobileNav.classList.remove("is-open");
    });
  });
}

// ---- Gallery carousel (mobile) ----
const carousel   = document.getElementById("work-carousel");
const prevBtn    = document.getElementById("carousel-prev");
const nextBtn    = document.getElementById("carousel-next");
const dots       = document.querySelectorAll(".carousel-dot");

if (carousel && prevBtn && nextBtn) {
  const getCardWidth = () => {
    const first = carousel.querySelector(".work-thumb");
    if (!first) return 0;
    const style = getComputedStyle(carousel);
    const gap   = parseFloat(style.gap) || 12;
    return first.offsetWidth + gap;
  };

  const scrollTo = (index) => {
    carousel.scrollTo({ left: getCardWidth() * index, behavior: "smooth" });
  };

  prevBtn.addEventListener("click", () => {
    const index = Math.round(carousel.scrollLeft / getCardWidth());
    scrollTo(Math.max(0, index - 1));
  });

  nextBtn.addEventListener("click", () => {
    const total = carousel.querySelectorAll(".work-thumb").length;
    const index = Math.round(carousel.scrollLeft / getCardWidth());
    scrollTo(Math.min(total - 1, index + 1));
  });

  // Update active dot on scroll
  carousel.addEventListener("scroll", () => {
    const index = Math.round(carousel.scrollLeft / getCardWidth());
    dots.forEach((dot, i) => dot.classList.toggle("is-active", i === index));
  }, { passive: true });

  // Dot click navigation
  dots.forEach((dot) => {
    dot.addEventListener("click", () => scrollTo(Number(dot.dataset.index)));
  });
}

// ---- FAQ accordion ----
document.querySelectorAll(".faq-question").forEach((btn) => {
  btn.addEventListener("click", () => {
    const expanded = btn.getAttribute("aria-expanded") === "true";
    const answer   = document.getElementById(btn.getAttribute("aria-controls"));

    // Close all others
    document.querySelectorAll(".faq-question").forEach((otherBtn) => {
      const otherAnswer = document.getElementById(otherBtn.getAttribute("aria-controls"));
      otherBtn.setAttribute("aria-expanded", "false");
      if (otherAnswer) otherAnswer.setAttribute("aria-hidden", "true");
    });

    // Toggle clicked
    if (!expanded) {
      btn.setAttribute("aria-expanded", "true");
      if (answer) answer.setAttribute("aria-hidden", "false");
    }
  });
});
