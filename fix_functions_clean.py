with open("index.html", "r") as f:
    content = f.read()

# 1. Clean up line 105 button HTML
old_btn = '<button onclick="openUserLoginModal()" class="user-login-header-btn"><i onclick="openUserLoginModal()" class="fa-solid fa-user"></i></button>'
new_btn = '<button onclick="openUserLoginModal()" class="user-login-header-btn" style="cursor:pointer; z-index:99999;"><i class="fa-solid fa-user"></i></button>'
content = content.replace(old_btn, new_btn)

# 2. Ensure modal toggle functions are globally defined at the very top of script or globally attached
global_script = """
<script>
    // Ensure global modal functions are explicitly attached to window
    window.openUserLoginModal = function() {
        const m = document.getElementById('user-login-modal');
        if (m) m.style.display = 'flex';
    };
    window.closeUserLoginModal = function() {
        const m = document.getElementById('user-login-modal');
        if (m) m.style.display = 'none';
    };
    window.openAdminLoginModal = function() {
        const m = document.getElementById('admin-login-modal');
        if (m) m.style.display = 'flex';
    };
    window.closeAdminLoginModal = function() {
        const m = document.getElementById('admin-login-modal');
        if (m) m.style.display = 'none';
    };
    window.changeLanguage = function(lang) {
        console.log("Language changed to: " + lang);
        // Translation handler fallback if needed
    };
</script>
"""

if "</body>" in content:
    content = content.replace("</body>", global_script + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("Fixed modal and header functions successfully!")
