import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace old floating trigger with "Ask Me" pill button
old_btn_pattern = r'<button class="floating-ai-trigger"[\s\S]*?</button>'
new_ask_btn = """<button class="floating-ai-trigger" onclick="toggleMadzinuAIChat()" title="Ask Madzinu AI" style="position: fixed; bottom: 20px; right: 20px; background: linear-gradient(135deg, #6366f1, #ec4899); color: #fff; border: none; padding: 10px 16px; border-radius: 30px; font-size: 11px; font-weight: bold; cursor: pointer; display: flex; align-items: center; gap: 6px; box-shadow: 0 4px 15px rgba(99, 102, 241, 0.5); z-index: 9999;">
    <i class="fa-solid fa-robot"></i> Ask Me
</button>"""

if re.search(old_btn_pattern, content):
    content = re.sub(old_btn_pattern, new_ask_btn, content)
else:
    # If not found, append before body close
    content = content.replace("</body>", new_ask_btn + "\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated floating AI button to 'Ask Me'!")
