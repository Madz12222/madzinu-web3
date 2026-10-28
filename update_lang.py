import re

with open('index.html', 'r', encoding='utf-8') as f:
    code = f.read()

# Add IDs to elements if missing or ensure full translation mapping
new_script_block = '''<script>
const translations = {
    EN: {
        brandTitle: "MADZINU WEB3 TECH & AI",
        adminBtn: "Admin",
        heroBadge: "INDIA'S FIRST AUTONOMOUS AI STUDIO & CLOUD NETWORK",
        heroTitle: "Sovereign Cloud Compute & Autonomous Jobworks",
        heroDesc: "Madzinu Web3 Technologies is a Govt. of India Recognized Startup entity under MeitY with approved IndiaAI Portal compute access. Provision high-throughput server compute packages from ₹2,000 to ₹1,00,000 with professional task remuneration over 14 days, manage live workspace balances, and execute daily automated jobworks.",
        launchTermBtn: "LAUNCH SECURE ENTERPRISE TERMINAL",
        waTitle: "10 Unique WhatsApp Referral Scripts",
        waDesc: "Share your referral link with auto-embedded ID:",
        voucherTitle: "Supported Voucher & Reward Partners",
        voucherSub: "* ENTERPRISE REWARD PARTNERS (API INTEGRATION & PILOT ROLLOUT COMING SOON)",
        goldTitle: "24K GOLD SHOWROOM PARTNERS (ENTERPRISE TIERS ₹25K+)",
        foodTitle: "INSTANT LIFESTYLE & FOOD VOUCHERS",
        officialWeb: "Official Website",
        feat1Title: "Daily E-Commerce Jobworks",
        feat1List: "<li><strong>Amazon:</strong> Fulfillment center node sync & SKU audit logs</li><li><strong>Flipkart:</strong> Logistics routing & pin-code serviceability checks</li><li><strong>Meesho:</strong> Catalog pricing verification & vendor order feeds</li><li><strong>MeitY Registered Startup Entity (Govt. of India)</strong></li><li><strong>Task Allocation & Professional Remuneration (14-Day Cycle)</strong></li>",
        feat2Title: "1. 14-Day Server Node License",
        feat2Desc: "Choose high-throughput cloud compute tiers (₹2,000 to ₹1,00,000 + 18% GST) with strict 14-day node validity and batch task workloads.",
        feat3Title: "2. Live Workspace Balance",
        feat3Desc: "Track real-time earned balance starting fresh at ₹0.00 directly inside your workspace terminal dashboard.",
        feat4Title: "3. E-Commerce Jobwork Tasks",
        feat4Desc: "Execute daily automated verification pipelines for Amazon, Flipkart, and Meesho to secure professional remuneration.",
        feat5Title: "4. 10% - 12% Dynamic Referral Bonus",
        feat5Desc: "Share your direct node activation link and earn a 10% base referral bonus (increases to 12% upon reaching 15 continuous active team members) credited instantly.",
        loginTitle: "Contractor Secure Node Login",
        phonePlaceholder: "Enter Mobile Number (e.g. 8122252222)",
        sendOtpBtn: "Send OTP",
        verifyOtpBtn: "Verify & Launch",
        bypassBtn: "Direct Login Bypass",
        dashActiveLbl: "Active Workspace Node",
        dashSubLbl: "Deploy a server node below to unlock assigned daily task batches over 14 days.",
        upgradeNodeBtn: "Purchase / Upgrade Server Node",
        workloadHeading: "Verified Operational Workloads",
        closeTermBtn: "Close Terminal",
        execBtn: "Start Sequential Execution",
        modalStoreTitle: "Select Server Node Subscription",
        modalStoreSub: "Each server tier assigns automated task batches and professional remuneration over a 14-day cycle. Includes dynamic referral bonus eligibility (up to 12%).",
        deployNodeBtn: "Deploy Selected Server Node via Razorpay",
        footerDisc: "<p>Madzinu Web3 Technologies — Govt. of India Recognized Startup Entity (MeitY) | IndiaAI Portal Approved (Reg No: ST20260926506)</p><p>Non-refundable 14-Day SaaS Cloud Computing & E-Commerce Jobwork Access. Remuneration based on assigned daily task workloads. Subject to Section 194TDS contractor guidelines & RazorpayX routing.</p>"
    },
    TE: {
        brandTitle: "మాడ్జినూ వెబ్3 టెక్ & AI",
        adminBtn: "అడ్మిన్",
        heroBadge: "భారతదేశపు మొదటి స్వయంప్రతిపత్తి కలిగిన AI స్టూడియో & క్లౌడ్ నెట్‌వర్క్",
        heroTitle: "సావెరిన్ క్లౌడ్ కమ్యూట్ & ఆటోనమస్ జాబ్‌వర్క్స్",
        heroDesc: "మాడ్జినూ వెబ్3 టెక్నాలజీస్ అనేది MeitY క్రింద గుర్తించబడిన స్టార్టప్. ₹2,000 నుండి ₹1,00,000 వరకు సర్వర్ ప్యాకేజీలను అందిస్తుంది.",
        launchTermBtn: "సెక్యూర్ ఎంటర్‌ప్రైజ్ టెర్మినల్‌ను లాంచ్ చేయండి",
        waTitle: "10 ప్రత్యేకమైన వాట్సాప్ రెఫరల్ స్క్రిప్ట్‌లు",
        waDesc: "ఆటో-ఎంబెడెడ్ IDతో మీ రెఫరల్ లింక్‌ని షేర్ చేయండి:",
        voucherTitle: "మద్దతు ఉన్న వౌచర్ & రివార్డ్ భాగస్వాములు",
        voucherSub: "* ఎంటర్‌ప్రైజ్ రివార్డ్ భాగస్వాములు (API ఇంటిగ్రేషన్ & పైలట్ రోల్‌అవుట్ త్వరలో వస్తుంది)",
        goldTitle: "24K గోల్డ్ షోరూమ్ భాగస్వాములు (ఎంటర్‌ప్రైజ్ టైర్స్ ₹25K+)",
        foodTitle: "తక్షణ లైఫ్‌స్టైల్ & ఫుడ్ వౌచర్‌లు",
        officialWeb: "అధికారిక వెబ్‌సైట్",
        feat1Title: "డైలీ ఇ-కామర్స్ జాబ్‌వర్క్స్",
        feat1List: "<li><strong>Amazon:</strong> నెట్‌వర్క్ సింక్ & SKU ఆడిట్ లాగ్‌లు</li><li><strong>Flipkart:</strong> లాజిస్టిక్స్ రూటింగ్ & పిన్‌కోడ్ తనిఖీలు</li>",
        feat2Title: "1. 14-రోజుల సర్వర్ నోడ్ లైసెన్స్",
        feat2Desc: "అధిక పనితీరు గల క్లౌడ్ కంప్యూట్ టైర్లను ఎంచుకోండి.",
        feat3Title: "2. లైవ్ వర్క్‌స్పేస్ బ్యాలెన్స్",
        feat3Desc: "₹0.00 నుండి ప్రారంభమయ్యే రియల్ టైమ్ ఆదాయాన్ని ట్రాక్ చేయండి.",
        feat4Title: "3. ఇ-కామర్స్ జాబ్‌వర్క్ టాస్క్‌లు",
        feat4Desc: "వృత్తిపరమైన వేతనాన్ని పొందడానికి ఆటోమేటెడ్ వెరిఫికేషన్ పైప్‌లైన్‌లను అమలు చేయండి.",
        feat5Title: "4. 10% - 12% డైనమిక్ రెఫరల్ బోనస్",
        feat5Desc: "10% బేస్ రెఫరల్ బోనస్ పొందండి (15 మంది క్రియాశీల సభ్యులను చేరుకున్నప్పుడు 12%కి పెరుగుతుంది).",
        loginTitle: "కాంట్రాక్టర్ సెక్యూర్ నోడ్ లాగిన్",
        phonePlaceholder: "మొబైల్ నంబర్‌ను నమోదు చేయండి",
        sendOtpBtn: "OTP పంపు",
        verifyOtpBtn: "ధృవీకరించండి & లాంచ్ చేయండి",
        bypassBtn: "డైరెక్ట్ లాగిన్ బైపాస్",
        dashActiveLbl: "యాక్టివ్ వర్క్‌స్పేస్ నోడ్",
        dashSubLbl: "14 రోజులకు రోజువారీ పనులను అన్‌లాక్ చేయడానికి సర్వర్ నోడ్‌ను డిప్లాయ్ చేయండి.",
        upgradeNodeBtn: "సర్వర్ నోడ్‌ను కొనుగోలు చేయండి / అప్‌గ్రేడ్ చేయండి",
        workloadHeading: "ధృవీకరించబడిన కార్యాచరణ పనులు",
        closeTermBtn: "టెర్మినల్ మూసివేయి",
        execBtn: "సీక్వెన్షియల్ ఎగ్జిక్యూషన్ ప్రారంభించు",
        modalStoreTitle: "సర్వర్ నోడ్ సబ్‌స్క్రిప్షన్‌ని ఎంచుకోండి",
        modalStoreSub: "ప్రతి సర్వర్ శ్రేణిలో ఆటోమేటెడ్ టాస్క్ బ్యాచ్‌లు ఉంటాయి.",
        deployNodeBtn: "Razorpay ద్వారా సర్వర్ నోడ్‌ని డిప్లాయ్ చేయండి",
        footerDisc: "<p>మాడ్జినూ వెబ్3 టెక్నాలజీస్ — MeitY గుర్తింపు పొందిన స్టార్టప్</p>"
    },
    TA: {
        brandTitle: "மாட்சினு வெப்3 டெக் & AI",
        adminBtn: "நிவாஹி",
        heroBadge: "இந்தியாவின் முதல் தன்னாட்சி AI ஸ்டுடியோ & கிளவுட் நெட்வொர்க்",
        heroTitle: "சவரன் கிளவுட் கம்ப்யூட் & தன்னாட்சி வேலைகள்",
        heroDesc: "மாட்சினு வெப்3 டெக்னாலஜிஸ் என்பது MeitY இன் கீழ் அங்கீகரிக்கப்பட்ட தொடக்கமாகும். ₹2,000 முதல் ₹1,00,000 வரை சர்வர் தொகுப்புகளை வழங்குகிறது.",
        launchTermBtn: "பாதுகாப்பான நிறுவன முனையத்தைத் தொடங்கு",
        waTitle: "10 பிரத்யேக வாட்ஸ்அப் ரெஃபரல் ஸ்கிரிப்ட்கள்",
        waDesc: "உங்கள் ரெஃபரல் இணைப்பை ஆட்டோ-எம்படெட் ஐடியுடன் பகிரவும்:",
        voucherTitle: "ஆதரிக்கப்படும் வவுச்சர் & பரிசு கூட்டாளிகள்",
        voucherSub: "* நிறுவன வெகுமதி கூட்டாளிகள் (API ஒருங்கிணைப்பு விரைவில் வரும்)",
        goldTitle: "24K தங்க ஷோரூம் கூட்டாளிகள் (நிறுவன அடுக்குகள் ₹25K+)",
        foodTitle: "உடனடி வாழ்க்கை முறை & உணவு வவுச்சர்கள்",
        officialWeb: "அதிகாரப்பூர்வ வலைத்தளம்",
        feat1Title: "தினசரி இ-காமர்ஸ் வேலைகள்",
        feat1List: "<li><strong>Amazon:</strong> நோடு ஒத்திசைவு & SKU தணிக்கை பதிவுகள்</li><li><strong>Flipkart:</strong> லாஜிஸ்டிக்ஸ் ரூட்டிங் & பின் கோடு சோதனைகள்</li>",
        feat2Title: "1. 14 நாள் சர்வர் நோடு உரிமம்",
        feat2Desc: "உயர் செயல்திறன் கொண்ட கிளவுட் கணக்கீட்டு அடுக்குகளைத் தேர்ந்தெடுக்கவும்.",
        feat3Title: "2. நேரலை பணிநிலை இருப்பு",
        feat3Desc: "₹0.00 இல் தொடங்கும் உண்மையான நேர வருவாயைக் கண்காணிக்கவும்.",
        feat4Title: "3. இ-காமர்ஸ் பணிப்பக்க பணிகள்",
        feat4Desc: "தொழில்முறை ஊதியத்தைப் பெற சரிபார்ப்பு குழாய்களை இயக்கவும்.",
        feat5Title: "4. 10% - 12% டைனமிக் பரிந்துரை போனஸ்",
        feat5Desc: "உங்கள் நேரடி இணைப்பு மூலம் 10% அடிப்படை பரிந்துரை போனஸ் பெறுக (15 செயலில் உள்ள உறுப்பினர்களை அடைந்தவுடன் 12% ஆக உயரும்).",
        loginTitle: "ஒப்பந்தக்காரர் பாதுகாப்பான நோடு உள்நுழைவு",
        phonePlaceholder: "மொபைல் எண்ணை உள்ளிடவும் (எ.கா. 8122252222)",
        sendOtpBtn: "OTP அனுப்பு",
        verifyOtpBtn: "சரிபார்த்து தொடங்குக",
        bypassBtn: "நேரடி உள்நுழைவு தவிர்ப்பு",
        dashActiveLbl: "செயலில் உள்ள பணிநிலை நோடு",
        dashSubLbl: "14 நாட்களுக்கு தினசரி பணிகளைத் திறக்க சர்வர் நோட்டைப் பயன்படுத்தவும்.",
        upgradeNodeBtn: "சர்வர் நோட்டை வாங்கவும் / மேம்படுத்தவும்",
        workloadHeading: "சரிபார்க்கப்பட்ட செயல்பாட்டு பணிகள்",
        closeTermBtn: "முனையத்தை மூடு",
        execBtn: "வரிசைமுறை செயலாக்கத்தைத் தொடங்கு",
        modalStoreTitle: "சர்வர் நோடு சந்தாவைத் தேர்ந்தெடுக்கவும்",
        modalStoreSub: "ஒவ்வொரு சர்வர் அடுக்கிலும் தானியங்கி பணித் தொகுப்புகள் உள்ளன.",
        deployNodeBtn: "Razorpay வழியாக சர்வர் நோட்டை வரிசைப்படுத்து",
        footerDisc: "<p>மாட்சினு வெப்3 டெக்னாலஜிஸ் — இந்தியாவின் அரசு அங்கீகரிக்கப்பட்ட Startup Entity (MeitY)</p>"
    },
    HI: {
        brandTitle: "माड्जिनू वेब3 टेक & AI",
        adminBtn: "एडमिन",
        heroBadge: "भारत का पहला स्वायत्त AI स्टूडियो और क्लाउड नेटवर्क",
        heroTitle: "सोवरिन क्लाउड कंप्यूट और स्वायत्त जॉबवर्क्स",
        heroDesc: "माड्जिनू वेब3 टेक्नोलॉजीज MeitY के तहत मान्यता प्राप्त स्टार्टअप है। यह ₹2,000 से ₹1,00,000 तक के सर्वर पैकेज प्रदान करता है।",
        launchTermBtn: "सुरक्षित एंटरप्राइज टर्मिनल लॉन्च करें",
        waTitle: "10 अद्वितीय व्हाट्सएप रेफरल स्क्रिप्ट",
        waDesc: "ऑटो-एम्बेडेड आईडी के साथ अपना रेफ़रल लिंक साझा करें:",
        voucherTitle: "समर्थित वाउचर और पुरस्कार भागीदार",
        voucherSub: "* एंटरप्राइज रिवार्ड पार्टनर (API इंटीग्रेशन और पायलट रोलआउट जल्द आ रहा है)",
        goldTitle: "24K गोल्ड शोरूम पार्टनर (एंटरप्राइज टियर ₹25K+)",
        foodTitle: "तत्काल लाइफस्टाइल और फूड वाउचर",
        officialWeb: "आधिकारिक वेबसाइट",
        feat1Title: "दैनिक ई-कॉमर्स जॉबवर्क्स",
        feat1List: "<li><strong>Amazon:</strong> नोड सिंक और SKU ऑडिट लॉग</li><li><strong>Flipkart:</strong> लॉजिस्टिक्स रूटिंग और पिन-कोड जांच</li>",
        feat2Title: "1. 14-दिवसीय सर्वर नोड लाइसेंस",
        feat2Desc: "उच्च-थ्रूपुट क्लाउड कंप्यूट टियर चुनें (₹2,000 से ₹1,00,000)।",
        feat3Title: "2. लाइव वर्कस्पेस बैलेंस",
        feat3Desc: "₹0.00 से शुरू होने वाली वास्तविक समय की कमाई को ट्रैक करें.",
        feat4Title: "3. ई-कॉमर्स जॉबवर्क कार्य",
        feat4Desc: "व्यावसायिक पारिश्रमिक सुरक्षित करने के लिए स्वचालित सत्यापन पाइपलाइन निष्पादित करें।",
        feat5Title: "4. 10% - 12% गतिशील रेफ़रल बोनस",
        feat5Desc: "10% बेस रेफ़रल बोनस अर्जित करें (15 सक्रिय सदस्यों तक पहुंचने पर 12% तक बढ़ जाता है)।",
        loginTitle: "कंट्रैक्टर सिक्योर नोड लॉगिन",
        phonePlaceholder: "मोबाइल नंबर दर्ज करें (जैसे 8122252222)",
        sendOtpBtn: "OTP भेजें",
        verifyOtpBtn: "सत्यापित करें और लॉन्च करें",
        bypassBtn: "प्रत्यक्ष लॉगिन बायपास",
        dashActiveLbl: "सक्रिय वर्कस्पेस नोड",
        dashSubLbl: "14 दिनों के दैनिक कार्यों को अनलॉक करने के लिए सर्वर नोड तैनात करें।",
        upgradeNodeBtn: "सर्वर नोड खरीदें / अपग्रेड करें",
        workloadHeading: "सत्यापित परिचालन कार्यभार",
        closeTermBtn: "टर्मिनल बंद करें",
        execBtn: "क्रमबद्ध निष्पादन शुरू करें",
        modalStoreTitle: "सर्वर नोड सदस्यता चुनें",
        modalStoreSub: "प्रत्येक सर्वर टियर 14-दिन के चक्र पर स्वचालित कार्य बैच प्रदान करता है।",
        deployNodeBtn: "Razorpay के माध्यम से सर्वर नोड तैनात करें",
        footerDisc: "<p>माड्जिनू वेब3 टेक्नोलॉजीज — MeitY मान्यता प्राप्त स्टार्टअप इकाई (भारत सरकार)</p>"
    }
};

let currentLang = 'EN';

function changeLanguage() {
    const selector = document.getElementById('langSelector') || document.querySelector('select');
    if(!selector) return;
    currentLang = selector.value;
    const t = translations[currentLang] || translations['EN'];

    if(document.getElementById('brand-title')) document.getElementById('brand-title').innerText = t.brandTitle;
    if(document.getElementById('admin-btn-txt')) document.getElementById('admin-btn-txt').innerText = t.adminBtn;
    if(document.getElementById('hero-badge')) document.getElementById('hero-badge').innerHTML = `<i class="fa-solid fa-crown"></i> ${t.heroBadge}`;
    if(document.getElementById('hero-title')) document.getElementById('hero-title').innerHTML = `Sovereign Cloud Compute & <br class="hidden md:block"/><span class="bg-gradient-to-r from-indigo-400 via-cyan-300 to-emerald-400 bg-clip-text text-transparent">Autonomous Jobworks</span>`;
    if(document.getElementById('hero-desc')) document.getElementById('hero-desc').innerText = t.heroDesc;
    if(document.getElementById('launch-term-btn')) document.getElementById('launch-term-btn').innerHTML = `<i class="fa-solid fa-arrow-right-to-bracket"></i> ${t.launchTermBtn}`;

    if(document.getElementById('wa-title')) document.getElementById('wa-title').innerText = t.waTitle;
    if(document.getElementById('wa-desc')) document.getElementById('wa-descchildNodes') || document.querySelector("p:has(#whatsapp-section) ~ p") ; // fallback text update
    
    // Update Voucher & Partner section headers if elements have specific selectors or query them
    document.querySelectorAll('h2, h3, h4, span, p').forEach(el => {
        if(el.innerText.trim() === 'Supported Voucher & Reward Partners') el.innerText = t.voucherTitle;
        if(el.innerText.includes('ENTERPRISE REWARD PARTNERS')) el.innerText = t.voucherSub;
        if(el.innerText.includes('24K GOLD SHOWROOM PARTNERS')) el.innerText = t.goldTitle;
        if(el.innerText.includes('INSTANT LIFESTYLE & FOOD VOUCHERS')) el.innerText = t.foodTitle;
        if(el.innerText.trim() === 'Official Website') el.innerText = t.officialWeb;
        if(el.innerText.trim() === '10 Unique WhatsApp Referral Scripts') el.innerText = t.waTitle;
        if(el.innerText.includes('Share your referral link with auto-embedded ID')) el.innerText = t.waDesc;
    });

    if(document.getElementById('feat-1-title')) document.getElementById('feat-1-title').innerHTML = `<i class="fa-solid fa-list-check text-indigo-400"></i> ${t.feat1Title}`;
    if(document.getElementById('feat-1-list')) document.getElementById('feat-1-list').innerHTML = t.feat1List;
    
    if(document.getElementById('feat-2-title')) document.getElementById('feat-2-title').innerHTML = `<i class="fa-solid fa-server text-indigo-400"></i> ${t.feat2Title}`;
    if(document.getElementById('feat-2-desc')) document.getElementById('feat-2-desc').innerText = t.feat2Desc;

    if(document.getElementById('feat-3-title')) document.getElementById('feat-3-title').innerHTML = `<i class="fa-solid fa-wallet text-emerald-400"></i> ${t.feat3Title}`;
    if(document.getElementById('feat-3-desc')) document.getElementById('feat-3-desc').innerText = t.feat3Desc;

    if(document.getElementById('feat-4-title')) document.getElementById('feat-4-title').innerHTML = `<i class="fa-solid fa-cart-shopping text-cyan-400"></i> ${t.feat4Title}`;
    if(document.getElementById('feat-4-desc')) document.getElementById('feat-4-desc').innerText = t.feat4Desc;

    if(document.getElementById('feat-5-title')) document.getElementById('feat-5-title').innerHTML = `<i class="fa-solid fa-users text-amber-400"></i> ${t.feat5Title}`;
    if(document.getElementById('feat-5-desc')) document.getElementById('feat-5-desc').innerText = t.feat5Desc;

    if(document.getElementById('login-title')) document.getElementById('login-title').innerHTML = `<i class="fa-solid fa-shield-keyhole text-indigo-400"></i> ${t.loginTitle}`;
    if(document.getElementById('login-identifier')) document.getElementById('login-identifier').placeholder = t.phonePlaceholder;
    if(document.getElementById('send-otp-btn')) document.getElementById('send-otp-btn').innerText = t.sendOtpBtn;
    if(document.getElementById('verify-otp-btn')) document.getElementById('verify-otp-btn').innerText = t.verifyOtpBtn;
    if(document.getElementById('bypass-btn-txt')) document.getElementById('bypass-btn-txt').innerHTML = `<i class="fa-solid fa-bolt"></i> ${t.bypassBtn}`;
    
    if(document.getElementById('dash-active-lbl')) document.getElementById('dash-active-lbl').innerText = t.dashActiveLbl;
    if(document.getElementById('dash-sub-lbl')) document.getElementById('dash-sub-lbl').innerText = t.dashSubLbl;
    if(document.getElementById('upgrade-node-btn')) document.getElementById('upgrade-node-btn').innerHTML = `<i class="fa-solid fa-server"></i> ${t.upgradeNodeBtn}`;
    if(document.getElementById('workload-heading')) document.getElementById('workload-heading').innerText = t.workloadHeading;
    if(document.getElementById('close-term-btn')) document.getElementById('close-term-btn').innerText = t.closeTermBtn;
    if(document.getElementById('exec-btn-txt')) document.getElementById('exec-btn-txt').innerText = t.execBtn;
    
    if(document.getElementById('modal-store-title')) document.getElementById('modal-store-title').innerText = t.modalStoreTitle;
    if(document.getElementById('modal-store-sub')) document.getElementById('modal-store-sub').innerText = t.modalStoreSub;
    if(document.getElementById('deploy-node-btn')) document.getElementById('deploy-node-btn').innerText = t.deployNodeBtn;
    if(document.getElementById('footer-disc')) document.getElementById('footer-disc').innerHTML = t.footerDisc;
}

document.addEventListener('DOMContentLoaded', () => {
    const sel = document.getElementById('langSelector') || document.querySelector('select');
    if(sel) {
        sel.onchange = changeLanguage;
    }
});
</script>'''

code = re.sub(r'<script>\s*const translations\s*=[\s\S]*?<\/script>', '', code)
code = code.replace('</body>', new_script_block + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully updated full multi-language translations!')
