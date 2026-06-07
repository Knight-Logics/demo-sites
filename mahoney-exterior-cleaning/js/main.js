(function () {
  function initHeaderScroll() {
    const header = document.querySelector(".site-header");
    if (!header) return;
    window.addEventListener(
      "scroll",
      () => header.classList.toggle("scrolled", window.scrollY > 40),
      { passive: true }
    );
  }

  function initMobileNav() {
    const toggle = document.querySelector(".nav-toggle");
    const nav = document.querySelector(".site-nav");
    const backdrop = document.querySelector(".nav-backdrop");
    if (!toggle || !nav) return;

    const setOpen = (open) => {
      nav.classList.toggle("open", open);
      backdrop?.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      document.body.classList.toggle("nav-open", open);
    };

    toggle.addEventListener("click", () => setOpen(!nav.classList.contains("open")));
    backdrop?.addEventListener("click", () => setOpen(false));
    nav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => setOpen(false));
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") setOpen(false);
    });
    setOpen(false);
  }

  function markActiveNav() {
    const path = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".site-nav a").forEach((link) => {
      const href = link.getAttribute("href");
      link.classList.toggle(
        "active",
        href === path || (path === "" && href === "index.html")
      );
    });
  }

  function initScrollReveal() {
    const revealEls = document.querySelectorAll(
      ".reveal, .reveal-left, .reveal-right, .reveal-scale, .reveal-photo"
    );
    if (!revealEls.length) return;

    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("visible");
              io.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
      );
      revealEls.forEach((el) => io.observe(el));
    } else {
      revealEls.forEach((el) => el.classList.add("visible"));
    }
  }

  function initHeroPanels() {
    document.querySelectorAll(".hero").forEach((hero) => {
      if (hero.dataset.panelsInit) return;
      hero.dataset.panelsInit = "1";
      requestAnimationFrame(() => hero.classList.add("hero-panels-ready"));
    });
  }

  function initQuoteForm() {
    const form = document.querySelector(".quote-form");
    if (!form) return;

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const status = form.querySelector(".form-status");
      if (status) {
        status.textContent =
          "Thanks — this demo form is not connected yet. Ryan will wire up live lead delivery before launch.";
        status.hidden = false;
      }
      form.reset();
    });
  }

  function init() {
    initHeaderScroll();
    initMobileNav();
    markActiveNav();
    initScrollReveal();
    initHeroPanels();
    initQuoteForm();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
