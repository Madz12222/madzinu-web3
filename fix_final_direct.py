with open("index.html", "r") as f:
    code = f.read()

# Replace the language select tag to ensure it calls changeLanguage correctly
old_select = '<select id="lang-select"'
new_select = '<select id="lang-select" onchange="window.changeLanguage(this.value)"'
if old_select in code:
    code = code.replace(old_select, new_select)

# Ensure the global changeLanguage function is robust and updates the DOM elements directly
translation_block = """
<script>
window.changeLanguage = function(lang) {
    const t = {
        EN: { title: "Autonomous Web3 Infrastructure & Cloud Node Operations", desc: "Deploy high-throughput microservices, manage validator node allocations, and access real-time decentralized automation tools." },
        TA: { title: "தன்னாட்சி Web3 உள்கட்டமைப்பு மற்றும் கிளவுட் முனை செயல்பாடுகள்", desc: "அதிக செயல்திறன் கொண்ட மைக்ரோசெர்வீஸ்களைப் பயன்படுத்துங்கள், சரிபார்ப்பு முனை ஒதுக்கீடுகளை நிர்வகிக்கவும்." },
        HI: { title: "স্বায়ত্তশাসিত Web3 অবকাঠামো এবং ক্লাউড নোড অপারেশন", desc: "उच्च-थ्रूपुट माइक्रोसेर्विसेज तैनात करें, वैनिडेटर नोड आवंटन प्रबंधित करें।" },
        TE: { title: "అటానమస్ Web3 ఇన్‌ఫ్రాస్ట్రక్చర్ & క్లౌడ్ నోడ్ ఆపరేషన్స్", desc: "అధిక-త్రూపుట్ మైక్రోసర్వీసెస్‌ని అమర్చండి, వ్యాలిడేటర్ నోడ్ కేటాయింపులను నిర్వహించండి." },
        ML: { title: "ഓട്ടോണമസ് Web3 ഇൻഫ്രാസ്ട്രക്ചർ & ക്ലൗഡ് നോഡ് പ്രവർത്തനങ്ങൾ", desc: "ഉയർന്ന ത്രൂപുട്ട് മൈക്രോസർവീസുകൾ വിന്യസിക്കുക, വാലിഡേറ്റർ നോഡ് അലോക്കേഷനുകൾ കൈകാര്യം ചെയ്യുക." },
        KN: { title: "ಸ್ವಾಯತ್ತ Web3 ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಕ್ಲೌಡ್ ನೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಳು", desc: "ಅಧಿಕ ಥ್ರೂಪುಟ್ ಮೈಕ್ರೋಸೆರ್ವಿಸುಗಳನ್ನು ನಿಯೋಜಿಸಿ, ವ್ಯಾಲಿಡೇಟರ್ ನೋಡ್ ಹಂಚಿಕೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ." }
    };
    const selected = t[lang] || t["EN"];
    
    const h1 = document.querySelector('h1');
    if (h1) h1.innerText = selected.title;

    const p = document.querySelector('.container p, p');
    if (p) p.innerText = selected.desc;
    
    console.log("Language updated to:", lang);
};
</script>
</body>
"""

if "</body>" in code:
    code = code.split("</body>")[0] + translation_block

with open("index.html", "w") as f:
    f.write(code)

print("Direct translation fix applied cleanly!")
