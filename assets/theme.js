(() => {
  const key = "prism-theme";
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  const root = document.documentElement;
  let preference;
  let toggle;

  try {
    const saved = localStorage.getItem(key);
    if (saved === "dark" || saved === "light") preference = saved;
  } catch {
    // The theme toggle still works when browser storage is unavailable.
  }

  const applyTheme = () => {
    const theme = preference || (system.matches ? "dark" : "light");
    root.dataset.theme = theme;
    if (toggle) toggle.selected = theme === "dark";
  };

  applyTheme();
  system.addEventListener("change", applyTheme);

  document.addEventListener("DOMContentLoaded", () => {
    toggle = document.querySelector(".theme-toggle:defined");
    if (!toggle) return;
    applyTheme();
    toggle.addEventListener("change", () => {
      preference = toggle.selected ? "dark" : "light";
      try {
        localStorage.setItem(key, preference);
      } catch {
        // Keep the choice for this page.
      }
      applyTheme();
    });
    toggle.hidden = false;
  });
})();
