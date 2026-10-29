with open("index.html", "r") as f:
    content = f.read()

# 1. Wrap the hero title and subtitle with proper data-i18n spans or IDs so they can be targeted
content = content.replace(
    '<h1 style=""',
    '<h1 id="hero-title-el" style=""'
)
content = content.replace(
    'Autonomous Web3 Infrastructure & Cloud Node Operations',
    '<span data-i18n="hero_title">Autonomous Web3 Infrastructure & Cloud Node Operations</span>'
)
content = content.replace(
    'Deploy high-throughput microservices, manage validator node allocations, and access real-time decentralized automation tools.',
    '<span data-i18n="hero_desc">Deploy high-throughput microservices, manage validator node allocations, and access real-time decentralized automation tools.</span>'
)

# 2. Re-write changeLanguage to instantly update innerText and alert confirmation
translation_handler = """
<script>
    const portalDict = {
        EN: {
            "hero_title": "Autonomous Web3 Infrastructure & Cloud Node Operations",
            "hero_desc": "Deploy high-throughput microservices, manage validator node allocations, and access real-time decentralized automation tools."
        },
        TA: {
            "hero_title": "தன்னாட்சி Web3 உள்கட்டமைப்பு மற்றும் கிளவுட் முனை செயல்பாடுகள்",
            "hero_desc": "அதிக செயல்திறன் கொண்ட மைக்ரோசெர்வீஸ்களைப் பயன்படுத்துங்கள், சரிபார்ப்பு முனை ஒதுக்கீடுகளை நிர்வகிக்கவும்."
        },
        HI: {
            "hero_title": "স্বায়ত্তশাসিত Web3 অবকাঠামো এবং ক্লাউড নোড অপারেশন",
            "hero_desc": "उच्च-थ्रूपुट माइक्रोसेर्विसेज तैनात करें, वैनिडेटर नोड आवंटन प्रबंधित करें।"
        },
        TE: {
            "hero_title": "అటానమస్ Web3 ఇన్‌ఫ్రాస్ట్రక్చర్ & క్లౌಡ್ నోడ్ ఆపరేషన్స్",
            "hero_desc": "అధిక-త్రూపుట్ మైక్రోసర్వీసెస్‌ని అమర్చండి, వ్యాలిడేటర్ నోడ్ కేటాయింపులను నిర్వహించండి."
        },
        ML: {
            "hero_title": "ഓട്ടോണമസ് Web3 ഇൻഫ്രാസ്ട്രക്ചർ & ക്ലൗഡ് നോഡ് പ്രവർത്തനങ്ങൾ",
            "hero_desc": "ഉയർന്ന ത്രൂപുട്ട് മൈക്രോസർവീസുകൾ വിന്യസിക്കുക, വാലിഡേറ്റർ നോഡ് അലോക്കേഷനുകൾ കൈകാര്യം ചെയ്യുക."
        },
        KN: {
            "hero_title": "ಸ್ವಾಯತ್ತ Web3 ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಕ್ಲೌಡ್ ನೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಳು",
            "hero_desc": "ಅಧಿಕ ಥ್ರೂಪುಟ್ ಮೈಕ್ರೋಸೆರ್ವಿಸುಗಳನ್ನು ನಿಯೋಜಿಸಿ, ವ್ಯಾಲಿಡೇಟರ್ ನೋಡ್ ಹಂಚಿಕೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ."
        }
    };

    window.changeLanguage = function(lang) {
        const dict = portalDict[lang] || portalDict["EN"];
        
        document.querySelectorAll("[data-i18n]").forEach(el => {
            const key = el.getAttribute("data-i18n");
            if (dict[key]) {
                el.innerText = dict[key];
            }
        });

        // Fallback direct update for header title
        const mainTitle = document.querySelector('h1');
        if (mainTitle && dict["hero_title"]) {
            mainTitle.innerHTML = dict["hero_title"];
        }

        console.log("Language switched to: " + lang);
    };
</script>
"""

if "</body>" in content:
    # Remove older translation script if present and append new one
    content = content.split('<script>\n    const portalTranslations')[0] + translation_handler + "\n</body>"

with open("index.html", "w") as f:
    f.write(content)

print("Deep translation fix applied!")
