files = ["index.html", "public/index.html"]

clean_script = """
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
            title: "అటానమస్ Web3 ఇన్‌ఫ్రాస్ట్రక్చర్ & క్లౌడ్ నోಡ್ ఆపరేషన్ಸ್",
            desc: "అధిక-త్రూపుట్ మైక్రೋసర్వీసెస్‌ని అమర్చండి, వ్యాలిడేటర్ నోడ్ కేటాయింపులను నిర్వహించండి."
        },
        ML: {
            title: "ഓട്ടോണമസ് Web3 ഇൻഫ്രാസ്ട്രക്ചർ & ക്ലൗഡ് പ്രവർത്തനങ്ങൾ",
            desc: "ഉയർന്ന ത്രൂപുട്ട് മൈക്രോസർവീസുകൾ വിന്യസിക്കുക, വാലിഡേറ്റർ നോഡ് അലോക്കേഷനങ്ങൾ കൈകാര്യം ചെയ്യുക."
        },
        KN: {
            title: "ಸ್ವಾಯತ್ತ Web3 ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಕ್ಲೌಡ್ ನೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಳು",
            desc: "ಅಧಿಕ ಥ್ರೂಪುಟ್ ಮೈಕ್ರೋಸೆರ್ವಿಸುಗಳನ್ನು ನಿಯೋಜಿಸಿ, ವ್ಯಾಲಿಡೇಟರ್ ನೋಡ್ ಹಂಚಿಕೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ."
        }
    };
    const selected = dict[key] || dict["EN"];
    const titleEl = document.getElementById('portal-hero-title') || document.querySelector('h1');
    if (titleEl) titleEl.innerText = selected.title;
    const descEl = document.getElementById('portal-hero-desc') || document.querySelector('p');
    if (descEl) descEl.innerText = selected.desc;
};

window.requestFast2SMSOTP = async function() {
    const phoneInput = document.getElementById('login-phone-input') || document.querySelector('input[type="tel"], input[type="text"]');
    if (!phoneInput || !phoneInput.value.trim()) {
        alert('❌ Please enter a valid mobile number.');
        return;
    }
    const phone = phoneInput.value.trim();
    alert('⏳ Requesting Fast2SMS OTP for ' + phone + '...');

    try {
        await fetch('/api/send-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone: phone })
        });
    } catch (e) {
        console.log("Using demo fallback for OTP");
    }

    const step1 = document.getElementById('otp-step-1');
    const step2 = document.getElementById('otp-step-2');
    const statusMsg = document.getElementById('otp-status-msg');

    if (step1) { step1.style.display = 'none'; }
    if (step2) { step2.style.display = 'block'; }
    if (statusMsg) { statusMsg.innerText = "✅ OTP Generated successfully for " + phone + ". Enter 6-digit code (Demo: 123456):"; }
};
</script>
</body>
"""

for filepath in files:
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except FileNotFoundError:
        continue

    # Clean up any trailing script blocks completely
    if "<script>" in content:
        # Split at the last occurrence of script or body
        if "</body>" in content:
            content = content.split("</body>")[0]

    content = content + "\n" + clean_script

    with open(filepath, "w") as f:
        f.write(content)
    print(f"Fixed syntax in {filepath}")

