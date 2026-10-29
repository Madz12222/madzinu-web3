with open("index.html", "r") as f:
    content = f.read()

# 1. Add direct CSS to force clickability on header controls
click_css = """
<style>
  header, .header, nav, select, button, .admin-btn-action, .btn-primary, #lang-select, [onclick] {
    pointer-events: auto !important;
    cursor: pointer !important;
  }
  .modal-overlay {
    pointer-events: auto;
  }
</style>
"""
if "</head>" in content:
    content = content.replace("</head>", click_css + "\n</head>")

# 2. Ensure the user profile icon / button has an explicit onclick handler to open the login modal
old_profile_btn = '<div class="profile-icon" ' # or whatever tag it is
# Let's target the green user icon in the header directly
content = content.replace(
    'class="fa-solid fa-user"', 
    'onclick="openUserLoginModal()" class="fa-solid fa-user"'
)
content = content.replace(
    '<div id="user-login-modal" class="modal-overlay">', 
    '<div id="user-login-modal" class="modal-overlay" style="display: none;">'
)

with open("index.html", "w") as f:
    f.write(content)

print("Fixed header button and dropdown clickability!")
