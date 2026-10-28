import re

with open("routes/jobworkRoutes.js", "r", encoding="utf-8") as f:
    content = f.read()

# Transporter configuration for Hostinger
transporter_config = """
const transporter = nodemailer.createTransport({
    host: 'smtp.hostinger.com',
    port: 465,
    secure: true,
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    }
});
"""

# Replace any existing transporter block or add standard Hostinger config
if "nodemailer.createTransport" in content:
    content = re.sub(
        r'const transporter = nodemailer\.createTransport\(\{[\s\S]*?\}\);',
        transporter_config.strip(),
        content
    )

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Updated routes/jobworkRoutes.js with Hostinger Direct SMTP configuration!")
