// Logo principal del encabezado: símbolo de gestión integral, seguridad y sostenibilidad.
const headerLogo = document.querySelector(".site-header .brand-mark");
if (headerLogo) {
  headerLogo.innerHTML = `
    <svg viewBox="0 0 64 64" aria-hidden="true">
      <circle cx="32" cy="32" r="27"></circle>
      <path d="M18 35c8-11 17-17 30-20-1 14-8 25-20 29-5 2-10-1-10-9Z"></path>
      <path d="M20 43c7-9 14-15 25-21"></path>
      <path d="m24 34 6 6 12-14"></path>
    </svg>`;
}

const menuToggle = document.getElementById("menuToggle");
const mainNav = document.getElementById("mainNav");

if (menuToggle && mainNav) {
  menuToggle.addEventListener("click", () => {
    mainNav.classList.toggle("open");
  });

  mainNav.querySelectorAll("a").forEach(a => {
    a.addEventListener("click", () => mainNav.classList.remove("open"));
  });
}

const modal = document.getElementById("serviceModal");
const modalContent = document.getElementById("modalContent");

document.querySelectorAll(".service-open").forEach(btn => {
  btn.addEventListener("click", () => {
    const id = btn.dataset.service;
    const data = document.getElementById(`data-${id}`);
    if (!data) return;

    modalContent.innerHTML = data.innerHTML;
    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  });
});

document.querySelectorAll("[data-close-modal]").forEach(el => {
  el.addEventListener("click", () => {
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  });
});

document.addEventListener("keydown", e => {
  if (e.key === "Escape" && modal?.classList.contains("open")) {
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }
});

const contactForm = document.getElementById("contactForm");
const formMessage = document.getElementById("formMessage");

if (contactForm) {
  contactForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const button = contactForm.querySelector("button[type='submit']");
    const originalText = button.textContent;
    button.disabled = true;
    button.textContent = "Enviando...";
    formMessage.className = "form-message";
    formMessage.textContent = "";

    const payload = Object.fromEntries(new FormData(contactForm).entries());

    try {
      const res = await fetch("/api/solicitudes", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      formMessage.textContent = data.mensaje;
      formMessage.classList.add(data.ok ? "success" : "error");

      if (data.ok) {
        contactForm.reset();
      }
    } catch (err) {
      formMessage.textContent = "No fue posible registrar la solicitud. Intenta nuevamente.";
      formMessage.classList.add("error");
    } finally {
      button.disabled = false;
      button.textContent = originalText;
    }
  });
}
