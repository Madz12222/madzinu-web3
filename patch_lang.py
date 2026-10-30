with open("index.html", "r") as f:
    content = f.read()

# Add IDs to sections if not present
content = content.replace('style="font-size: 11px;">\n            <div style="font-weight: bold; color: #818cf8;', 'id="feat-box" style="font-size: 11px;">\n            <div id="feat-title" style="font-weight: bold; color: #818cf8;')
content = content.replace('Supported Voucher & Reward Partners', '<span id="partner-header">Supported Voucher & Reward Partners</span>')
content = content.replace('Contractor Secure Node Login', '<span id="login-header">Contractor Secure Node Login</span>')

with open("index.html", "w") as f:
    f.write(content)

print("HTML structure patched for full translation!")
