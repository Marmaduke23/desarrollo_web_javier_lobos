document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("tbody tr[data-form]").forEach(row => {
    row.addEventListener("click", () => {
      const formId = row.getAttribute("data-form");
      const form = document.getElementById(formId);
      if (form) form.submit();
    });
  });
});
