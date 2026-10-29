with open("index.html", "r") as f:
    code = f.read()

# Replace the changeLanguage function to automatically uppercase the language key
new_func = """
<script>
window.changeLanguage = function(lang) {
    const key = (lang || "EN").toUpperCase();
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
            desc: "అధిక-త్రూపుట్ మైక్రೋసర్వీసెస్‌ని అమర్చండి, వ్యాలిడేటర్ నోడ్ కేటాయింపులను నిర్వహించండి."
        },
        ML: {
            title: "ഓട്ടോണമസ് Web3 ഇൻഫ്രാസ്ട്രക്ചർ & ക്ലൗഡ് നോഡ് പ്രവർത്തനങ്ങൾ",
            desc: "ഉയർന്ന ത്രൂപുട്ട് മൈക്രോസർവീസുകൾ വിന്യസിക്കുക, വാലിഡേറ്റർ നോഡ് അലോക്കേഷനങ്ങൾ കൈകാര്യം ചെയ്യുക."
        },
        KN: {
            title: "ಸ್ವಾಯತ್ತ Web3 ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಕ್ಲೌಡ್ ನೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಳು",
            desc: "ಅಧಿಕ ಥ್ರೂಪುಟ್ ಮೈಕ್ರೋಸೆರ್ವಿಸುಗಳನ್ನು ನಿಯೋಜಿಸಿ, ವ್ಯಾಲಿಡೇಟರ್ ನೋಡ್ ಹಂಚಿಕೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ."
        }
    };

    const selected = dict[key] || dict["EN"];
    
    const titleEl = document.getElementById('portal-hero-title');
    if (titleEl) titleEl.innerText = selected.title;

    const descEl = document.getElementById('portal-hero-desc');
    if (descEl) descEl.innerText = selected.desc;

    console.log("Language successfully switched to:", key);
};
</script>
"""

# Replace existing changeLanguage script block if present, or append before </body>
if "window.changeLanguage = function" in code:
    # Remove old changeLanguage script block
    parts = code.split("<script>\nwindow.changeLanguage = function")
    code = parts[0] + new_func + "\n</body>"
elif "</head>" in code:
    code = code.replace("</head>", new_func + "\n</head>")

with open("index.html", "w") as f:
    f.write(code)

print("Language uppercase mapping fix applied successfully!")
