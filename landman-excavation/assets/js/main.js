document.querySelectorAll("#year").forEach((el) => {
  el.textContent = String(new Date().getFullYear());
});

const header = document.querySelector(".site-header");
if (header) {
  const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

const drawer = document.querySelector(".drawer");
const scrim = document.querySelector(".scrim");
const openBtn = document.querySelector(".hamburger");
const closeBtn = document.querySelector(".drawer-close");

function setDrawer(open) {
  if (!drawer || !scrim || !openBtn) return;
  drawer.classList.toggle("open", open);
  scrim.classList.toggle("open", open);
  openBtn.setAttribute("aria-expanded", open ? "true" : "false");
  drawer.toggleAttribute("inert", !open);
  document.body.style.overflow = open ? "hidden" : "";
}
openBtn?.addEventListener("click", () => setDrawer(true));
closeBtn?.addEventListener("click", () => setDrawer(false));
scrim?.addEventListener("click", () => setDrawer(false));
drawer?.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setDrawer(false)));

document.querySelectorAll(".estimate-form").forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    form.hidden = true;
    const ok = form.parentElement.querySelector(".form-ok");
    if (ok) ok.classList.add("show");
  });
});
