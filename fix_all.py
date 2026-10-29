with open("index.html", "r") as f:
    text = f.read()

# Ensure modal overlay CSS allows clicks when hidden or fixes pointer events
if ".modal-overlay {" in text:
    text = text.replace(".modal-overlay {", ".modal-overlay { pointer-events: auto;")

# Ensure language selector is fully interactive and has the proper change event
if 'onchange="changeLanguage' not in text and '<select' in text:
    text = text.replace('<select>', '<select id="lang-select" onchange="changeLanguage(this.value)">')

with open("index.html", "w") as f:
    f.write(text)

print("HTML fixed successfully!")
