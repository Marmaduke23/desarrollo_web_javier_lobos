document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("tr[data-url]").forEach(row => {
        row.addEventListener("click", function() {
            window.location.href = this.dataset.url;
        });
    });
});