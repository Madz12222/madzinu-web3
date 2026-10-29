with open("index.html", "r") as f:
    content = f.read()

# 1. Ensure language dropdown has proper id and onchange handler
content = content.replace('onchange="changeLanguage(this.value)"', 'id="lang-select" onchange="changeLanguage(this.value)"')

# 2. Tag key elements with data-i18n attributes if missing
content = content.replace('Autonomous Web3 Infrastructure & Cloud Node Operations', '<span data-i18n="hero_title">Autonomous Web3 Infrastructure & Cloud Node Operations</span>')
content = content.replace('Access Portal Dashboard', '<span data-i18n="btn_dashboard">Access Portal Dashboard</span>')
content = content.replace('Platform Core Architecture', '<span data-i18n="arch_header">Platform Core Architecture</span>')

# 3. Inject full 6-language translation engine before </body>
translation_script = """
<script>
    const portalTranslations = {
        EN: {
            "hero_title": "Autonomous Web3 Infrastructure & Cloud Node Operations",
            "btn_dashboard": "Access Portal Dashboard",
            "arch_header": "Platform Core Architecture"
        },
        TA: {
            "hero_title": "தன்னாட்சி Web3 உள்கட்டமைப்பு மற்றும் கிளவுட் முனை செயல்பாடுகள்",
            "btn_dashboard": "போர்டல் டாஷ்போர்டை அணுகவும்",
            "arch_header": "மேடை கோர் கட்டமைப்பு"
        },
        HI: {
            "hero_title": "স্বায়ত্তশাসিত Web3 অবকাঠামো এবং ক্লাউড নোড অপারেশন",
            "btn_dashboard": "पोर्टल डैशबोर्ड तक पहुंचें",
            "arch_header": "प्लेटफ़ॉर्म कोर वास्तुकला"
        },
        TE: {
            "hero_title": "అటానమస్ Web3 ఇన్‌ఫ్రాస్ట్రక్చర్ & క్లౌడ్ నోడ్ ఆపరేషన్స్",
            "btn_dashboard": "పోర్టల్ డాష్‌బోర్డ్‌ని యాక్సెస్ చేయండి",
            "arch_header": "ప్లాట్‌ఫారమ్ కోర్ ఆర్కిటెక్చర్"
        },
        ML: {
            "hero_title": "ഓട്ടോണമസ് Web3 ഇൻഫ്രാസ്ട്രക്ചർ & ക്ലൗഡ് നോഡ് പ്രവർത്തനങ്ങൾ",
            "btn_dashboard": "പോർട്ടൽ ഡാഷ്‌ബോർഡ് ആക്സസ് ചെയ്യുക",
            "arch_header": "പ്ലാറ്റ്‌ഫോം കോർ ആർക്കിടെക്ചർ"
        },
        KN: {
            "hero_title": "ಸ್ವಾಯತ್ತ Web3 ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಕ್ಲೌಡ್ ನೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಳು",
            "btn_dashboard": "ಪೋರ್ಟಲ್ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ಅನ್ನು ಪ್ರವೇಶಿಸಿ",
            "arch_header": "ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಕೋರ್ ಆರ್ಕಿടെക്ಚർ"
        }
    };

    window.changeLanguage = function(lang) {
        const dict = portalTranslations[lang] || portalTranslations["EN"];
        document.querySelectorAll("[data-i18n]").forEach(el => {
            const key = el.getAttribute("data-i18n");
            if (dict[key]) {
                el.innerText = dict[key];
            }
        });
        console.log("Language successfully switched to: " + lang);
    };
</script>
"""

if "</body>" in content:
    content = content.replace("</body>", translation_script + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("Translation engine applied successfully!")
