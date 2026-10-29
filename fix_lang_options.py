with open("index.html", "r") as f:
    html = f.read()

# 1. Ensure the select tag has the proper id and onchange handler
if 'id="lang-select"' not in html:
    html = html.replace('<select', '<select id="lang-select" onchange="changeLanguage(this.value)"')
else:
    html = html.replace('onchange=', 'data-old-oc=').replace('<select', '<select id="lang-select" onchange="changeLanguage(this.value)"')

# 2. Add IDs to the main hero title and description so we can target them 100% reliably
html = html.replace('Autonomous Web3 Infrastructure & Cloud Node Operations', '<span id="portal-hero-title">Autonomous Web3 Infrastructure & Cloud Node Operations</span>')
html = html.replace('Deploy high-throughput microservices, manage validator node allocations, and access real-time decentralized automation tools.', '<span id="portal-hero-desc">Deploy high-throughput microservices, manage validator node allocations, and access real-time decentralized automation tools.</span>')

# 3. Inject the robust translation engine right before </head>
translation_engine = """
<script>
window.changeLanguage = function(lang) {
    const dict = {
        EN: {
            title: "Autonomous Web3 Infrastructure & Cloud Node Operations",
            desc: "Deploy high-throughput microservices, manage validator node allocations, and access real-time decentralized automation tools."
        },
        TA: {
            title: "தன்னாட்சி Web3 உள்கட்டமைப்பு மற்றும் கிளவுட் முனை செயல்பாடுகள்",
            desc: "அதிக செயல்திறன் கொண்ட மைக்ரோசெர்வீஸ்களைப் பயன்படுத்துங்கள், சரிபார்ப்பு முனை ஒதுக்கீடுகளை நிர்வகிக்கவும்."
        },
        HI: {
            title: "স্বায়ত্তশাসিত Web3 অবকাঠামো এবং ক্লাউড নোড অপারেশন",
            desc: "उच्च-थ्रूपुट माइक्रोसेर्विसेज तैनात करें, वैनिडेटर नोड आवंटन प्रबंधित करें।"
        },
        TE: {
            title: "అటానమస్ Web3 ఇన్‌ఫ్రాస్ట్రక్చర్ & క్లౌడ్ నోಡ್ ఆపరేషన్స్",
            desc: "అధిక-త్రూపుట్ మైక్రోసర్వీసెస్‌ని అమర్చండి, వ్యాలిడేటర్ నోడ్ కేటాయింపులను నిర్వహించండి."
        },
        ML: {
            title: "ഓട്ടോണമസ് Web3 ഇൻഫ്രാസ്ട്രക്ചർ & ക്ലൗഡ് നോഡ് പ്രവർത്തനങ്ങൾ",
            desc: "ഉയർന്ന ത്രൂപുട്ട് മൈക്രോസർവീസുകൾ വിന്യസിക്കുക, വാലിഡേറ്റർ നോഡ് അലോക്കേഷനുകൾ കൈകാര്യം ചെയ്യുക."
        },
        KN: {
            title: "ಸ್ವಾಯತ್ತ Web3 ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಕ್ಲೌಡ್ ನೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಳು",
            desc: "ಅಧಿಕ ಥ್ರೂಪುಟ್ ಮೈಕ್ರೋಸೆರ್ವಿಸುಗಳನ್ನು ನಿಯೋಜಿಸಿ, ವ್ಯಾಲಿಡೇಟರ್ ನೋಡ್ ಹಂಚಿಕೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ."
        }
    };

    const selected = dict[lang] || dict["EN"];
    
    const titleEl = document.getElementById('portal-hero-title');
    if (titleEl) titleEl.innerText = selected.title;

    const descEl = document.getElementById('portal-hero-desc');
    if (descEl) descEl.innerText = selected.desc;

    console.log("Language switched successfully to:", lang);
};
</script>
"""

if "</head>" in html:
    html = html.replace("</head>", translation_engine + "\n</head>")

with open("index.html", "w") as f:
    f.write(html)

print("Translation engine and option bindings updated successfully!")
