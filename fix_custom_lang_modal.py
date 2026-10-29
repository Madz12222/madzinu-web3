with open("index.html", "r") as f:
    content = f.read()

# 1. Replace the custom language modal items / text containers to have direct onclick handlers
# Let's target the language names shown in the modal popup screenshot
languages = [
    ("EN", "EN"),
    ("தமிழ்", "TA"),
    ("हिन्दी", "HI"),
    ("తెలుగు", "TE"),
    ("മലയാളം", "ML"),
    ("ಕನ್ನಡ", "KN")
]

for label, code in languages:
    # Look for elements containing the language label inside the modal and add onclick
    old_html = f'>{label}<'
    new_html = f' onclick="changeLanguage(\'{code}\')" style="cursor: pointer;">{label}<'
    if old_html in content and f"changeLanguage('{code}')" not in content:
        content = content.replace(old_html, new_html, 1)

# 2. Ensure changeLanguage updates the UI text and closes the modal
translation_script = """
<script>
window.changeLanguage = function(lang) {
    const t = {
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
            title: "అటానమస్ Web3 ఇన్‌ఫ్రాస్ట్రక్చర్ & క్లౌడ్ నోడ్ ఆపరేషన్స్", 
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
    
    const selected = t[lang] || t["EN"];
    
    // Update main hero title
    const h1 = document.querySelector('h1');
    if (h1) h1.innerText = selected.title;

    // Update hero description
    const p = document.querySelector('h1 + p, .container p, p');
    if (p) p.innerText = selected.desc;

    // Update the button text showing current language if any
    const langBtnText = document.getElementById('current-lang-text');
    if (langBtnText) langBtnText.innerText = lang;

    // Close the language modal if open
    const modals = document.querySelectorAll('.modal-overlay, div[id*="lang"], div[id*="modal"]');
    modals.forEach(m => {
        if (m.style && (m.style.display === 'flex' || m.style.display === 'block')) {
            // Check if it is the language modal
            if (m.innerHTML.includes('தமிழ்') || m.innerHTML.includes('हिन्दी')) {
                m.style.display = 'none';
            }
        }
    });

    console.log("Language successfully changed to: " + lang);
    alert('🌐 Language switched to ' + lang);
};
</script>
"""

if "</body>" in content:
    content = content.split("</script>\n</body>")[0] + "\n" + translation_script + "\n</body>"

with open("index.html", "w") as f:
    f.write(content)

print("Custom language modal click handlers applied!")
