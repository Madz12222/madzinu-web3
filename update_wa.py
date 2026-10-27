with open("index.html", "r") as f:
    content = f.read()

wa_code = """
<div style="margin-top: 15px; background: #0d1322; padding: 12px; border-radius: 10px; border: 1.5px solid #1f2937;">
    <h3 style="font-size: 11px; color: #34d399; margin-bottom: 6px;">📱 WhatsApp Referral Scripts</h3>
    <button style="background: #166534; color: white; border: none; padding: 8px; width: 100%; border-radius: 6px; font-weight: bold; font-size: 11px; cursor: pointer;" onclick="window.open('https://api.whatsapp.com/send?text=Join%20Madzinu%20Web3%20Technologies%20https://madzinuweb3technologies.in', '_blank')">Share on WhatsApp</button>
</div>
"""

if "WhatsApp Referral Scripts" not in content:
    content = content.replace("</body>", wa_code + "\n</body>")
    with open("index.html", "w") as f:
        f.write(content)
    print("WhatsApp button added successfully!")
else:
    print("Already added!")
