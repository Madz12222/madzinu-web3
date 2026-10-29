with open("index.html", "r") as f:
    content = f.read()

# 1. Inject robust CSS to ensure header, buttons, and select dropdown are completely unblocked and on top
css_fix = """
<style>
  /* Force all pointer events and top layer priority */
  body {
    position: relative;
    pointer-events: auto !important;
  }
  header, .header, nav, .top-bar {
    position: relative !important;
    z-index: 999999 !important;
    pointer-events: auto !important;
  }
  button, select, input, .user-login-header-btn, .admin-header-btn, #lang-select {
    position: relative !important;
    z-index: 1000000 !important;
    pointer-events: auto !important;
    cursor: pointer !important;
  }
  .modal-overlay {
    z-index: 2000000 !important;
  }
</style>
"""

if "</head>" in content:
    content = content.replace("</head>", css_fix + "\n</head>")

# 2. Inject explicit event listeners right before </body> to bind clicks dynamically
js_fix = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    const userBtn = document.querySelector('.user-login-header-btn');
    if (userBtn) {
        userBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const m = document.getElementById('user-login-modal');
            if (m) m.style.display = 'flex';
        });
    }

    const adminBtn = document.querySelector('.admin-header-btn');
    if (adminBtn) {
        adminBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const m = document.getElementById('admin-login-modal');
            if (m) m.style.display = 'flex';
        });
    }

    const langSelect = document.getElementById('lang-select');
    if (langSelect) {
        langSelect.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
});
</script>
</body>
"""

if "</body>" in content:
    content = content.replace("</body>", js_fix)

with open("index.html", "w") as f:
    f.write(content)

print("Ultimate click fix applied successfully!")
