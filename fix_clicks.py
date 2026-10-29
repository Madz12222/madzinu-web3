with open("index.html", "r") as f:
    content = f.read()

# Ensure all modal overlays default to display: none and don't block pointer events when closed
if "class=\"modal-overlay\"" in content:
    content = content.replace(
        '.modal-overlay {',
        '.modal-overlay { display: none; pointer-events: auto;'
    )

# Fix language selector functionality to ensure it is fully clickable
old_lang_select = '<select id="lang-select"'
if old_lang_select not in content:
    # Add an id to the language dropdown if missing
    content = content.replace(
        '<select onchange="changeLanguage(this.value)">',
        '<select id="lang-select" onchange="changeLanguage(this.value)">'
    )

with open("index.html", "w") as f:
    f.write(content)

print("Applied click & interactivity fix!")
