with open("index.html", "r") as f:
    content = f.read()

# 1. Fix modal overlays so they don't block clicks when hidden
content = content.replace("display: flex;", "display: none;")
content = content.replace("display:block;", "display:none;")

# 2. Ensure CSS for modals has pointer-events set correctly
if "pointer-events" not in content:
    content = content.replace("</style>", "  .modal-overlay { pointer-events: none; }\n  .modal-overlay.active, div[style*='display: flex'] { pointer-events: auto; }\n</style>")

# 3. Ensure language dropdown and header buttons have explicit high z-index and pointer events
header_fix = """
<style>
  header, .header, nav, select, button, .admin-btn-action, .btn-primary {
    position: relative;
    z-index: 99999 !important;
    pointer-events: auto !important;
  }
  .modal-overlay {
    z-index: 100000 !important;
  }
</style>
"""
if "</head>" in content:
    content = content.replace("</head>", header_fix + "\n</head>")

with open("index.html", "w") as f:
    f.write(content)

print("Applied deep clickability fix successfully!")
