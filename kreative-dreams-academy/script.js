const currentYear = document.getElementById("current-year");

if (currentYear) {
  currentYear.textContent = new Date().getFullYear();
}

const revealItems = document.querySelectorAll("[data-reveal]");

if ("IntersectionObserver" in window && revealItems.length > 0) {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    {
      threshold: 0.18,
      rootMargin: "0px 0px -40px 0px",
    },
  );

  revealItems.forEach((item) => revealObserver.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

const previewForm = document.getElementById("hero-contact-form");
const formSuccess = document.getElementById("form-success");

if (previewForm && formSuccess) {
  previewForm.addEventListener("submit", (event) => {
    event.preventDefault();
    previewForm.hidden = true;
    formSuccess.hidden = false;
  });
}

document.querySelectorAll(".faq-question").forEach((button) => {
  button.addEventListener("click", () => {
    const isExpanded = button.getAttribute("aria-expanded") === "true";
    const answer = document.getElementById(button.getAttribute("aria-controls"));

    document.querySelectorAll(".faq-question").forEach((otherButton) => {
      const otherAnswer = document.getElementById(otherButton.getAttribute("aria-controls"));
      otherButton.setAttribute("aria-expanded", "false");

      if (otherAnswer) {
        otherAnswer.setAttribute("aria-hidden", "true");
        otherAnswer.setAttribute("inert", "");
      }
    });

    button.setAttribute("aria-expanded", String(!isExpanded));

    if (answer) {
      answer.setAttribute("aria-hidden", String(isExpanded));

      if (isExpanded) {
        answer.setAttribute("inert", "");
      } else {
        answer.removeAttribute("inert");
      }
    }
  });
});

const hamburgerButton = document.getElementById("hamburger-btn");
const mobileNav = document.getElementById("mobile-nav");
const mobileNavClose = document.getElementById("mobile-nav-close");
const navOverlay = document.getElementById("nav-overlay");

function openMobileNav() {
  if (!mobileNav || !navOverlay || !hamburgerButton) {
    return;
  }

  mobileNav.classList.add("is-open");
  navOverlay.classList.add("is-open");
  hamburgerButton.classList.add("is-open");
  hamburgerButton.setAttribute("aria-expanded", "true");
  mobileNav.setAttribute("aria-hidden", "false");
  mobileNav.removeAttribute("inert");
  document.body.style.overflow = "hidden";
}

function closeMobileNav() {
  if (!mobileNav || !navOverlay || !hamburgerButton) {
    return;
  }

  mobileNav.classList.remove("is-open");
  navOverlay.classList.remove("is-open");
  hamburgerButton.classList.remove("is-open");
  hamburgerButton.setAttribute("aria-expanded", "false");
  mobileNav.setAttribute("aria-hidden", "true");
  mobileNav.setAttribute("inert", "");
  document.body.style.overflow = "";
}

if (hamburgerButton) {
  hamburgerButton.addEventListener("click", () => {
    if (hamburgerButton.classList.contains("is-open")) {
      closeMobileNav();
    } else {
      openMobileNav();
    }
  });
}

if (mobileNavClose) {
  mobileNavClose.addEventListener("click", closeMobileNav);
}

if (navOverlay) {
  navOverlay.addEventListener("click", closeMobileNav);
}

if (mobileNav) {
  mobileNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", closeMobileNav);
  });
}