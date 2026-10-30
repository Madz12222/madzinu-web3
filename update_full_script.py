with open("index.html", "r") as f:
    code = f.read()

# New comprehensive translation script block
new_js = """
    <script>
        const translations = {
            'EN': {
                badge: "👑 INDIA'S FIRST AUTONOMOUS AI STUDIO & CLOUD NETWORK",
                title: 'Sovereign Cloud Compute &<br><span>Autonomous Jobworks & Live Gold Vault</span>',
                desc: 'Madzinu Web3 Technologies is a Govt. of India Recognized Startup entity under MeitY with approved IndiaAI Portal compute access. Provision high-throughput server compute packages from ₹2,000 to ₹1,00,000.',
                launchBtn: 'LAUNCH SECURE ENTERPRISE TERMINAL',
                featTitle: 'Platform Ecosystem Features',
                feat1: 'Free Tier: Earn ₹25 daily for 4 days per mobile number (Total ₹100, Min Withdraw ₹100).',
                feat2: 'Server Packages: Tiers ranging from ₹2,000 to ₹1,00,000 (+18% GST) with 14-day cycle.',
                feat3: '3-Tier Referral: Silver (10%) → Gold (12%) → Diamond (15%) instant commission.',
                waTitle: '10 Unique WhatsApp Referral Scripts',
                waDesc: 'Share your referral link with auto-embedded ID:',
                partnerTitle: 'Supported Voucher & Reward Partners',
                partnerSub: '* ENTERPRISE REWARD PARTNERS (API INTEGRATION & PILOT ROLLOUT COMING SOON)',
                goldTitle: '24K GOLD SHOWROOM PARTNERS (ENTERPRISE TIERS ₹25K+)',
                foodTitle: 'INSTANT LIFESTYLE & FOOD VOUCHERS',
                loginTitle: 'Contractor Secure Node Login',
                loginPlaceholder: 'Enter Mobile Number',
                loginBtn: 'Login',
                wa: [
                    "🚀 Join Madzinu Web3 Technologies - Govt recognized cloud compute & 24K Gold Vault rewards! Check out: ",
                    "💎 Invest in Sovereign Cloud & 24K Gold Showroom Vouchers (Tanishq/GRT). Start today: ",
                    "💼 Execute Daily E-Commerce Jobworks (Amazon/Flipkart/Meesho) & earn daily payouts! Join here: ",
                    "🌟 MeitY Recognized Startup (Govt of India) offering high-throughput server nodes & daily remuneration: ",
                    "💰 Build your secure digital asset portfolio with Madzinu Web3 Technologies. Explore compute tiers: ",
                    "🏆 Unlock 24K Gold Showroom Partners & secure daily task income. Check out now: ",
                    "🔒 Secure Enterprise Terminal & automated verification pipelines. Join the network: ",
                    "🎁 Earn 10%-12% referral bonuses & daily task payouts with Madzinu Web3: ",
                    "🤖 Powered by Madzinu AI Studio & Cloud Network. Experience autonomous jobworks: ",
                    "📈 Scale your earnings with 14-day server node licenses and secure cloud compute: "
                ]
            },
            'TA': {
                badge: "👑 இந்தியாவின் முதல் சுயாதீன ஏஐ ஸ்டுடியோ & கிளவுட் நெட்வொர்க்",
                title: 'சவரன் கிளவுட் கம்ப்யூட் &<br><span>தன்னாட்சி பணி மற்றும் லைவ் கோல்டு வால்ட்</span>',
                desc: 'மாட்ஜினு வெப்3 டெக்னாலஜிஸ் என்பது மீட்டி (MeitY) கீழ் அங்கீகரிக்கப்பட்ட ஸ்டார்ட்அப் நிறுவனமாகும். ₹2,000 முதல் ₹1,00,000 வரையிலான கிளவுட் கம்ப்யூட் பேக்கேஜ்கள் வழங்கப்படுகின்றன.',
                launchBtn: 'பாதுகாப்பான என்டர்பிரைஸ் டெர்மினலைத் தொடங்கவும்',
                featTitle: 'பிளாட்ஃபார்ம் சுற்றுச்சூழல் அம்சங்கள்',
                feat1: 'இலவச அடுக்கு: மொபைல் எண்ணுக்கு 4 நாட்களுக்கு தினமும் ₹25 சம்பாதிக்கவும் (மொத்தம் ₹100, குறைந்தபட்ச திரும்பப் பெறுதல் ₹100).',
                feat2: 'சர்வர் தொகுப்புகள்: ₹2,000 முதல் ₹1,00,000 வரையிலான அடுக்குகள் (+18% ஜிஎஸ்டி) 14 நாள் சுழற்சியுடன்.',
                feat3: '3-அடுக்கு பரிந்துரை: வெள்ளி (10%) → தங்கம் (12%) → வைரம் (15%) உடனடி கமிஷன்.',
                waTitle: '10 தனித்துவமான வாட்ஸ்அப் பரிந்துரை ஸ்கிரிப்டுகள்',
                waDesc: 'தானியங்கி ஐடியுடன் உங்கள் பரிந்துரை இணைப்பைப் பகிரவும்:',
                partnerTitle: 'ஆதரிக்கப்படும் வவுச்சர் மற்றும் வெகுமதி கூட்டாளிகள்',
                partnerSub: '* எண்டர்பிரைஸ் ரிவார்ட் பார்ட்னர்கள் (ஏபிஐ ஒருங்கிணைப்பு & பைலட் வெளியீடு விரைவில்)',
                goldTitle: '24K தங்க ஷோரூம் கூட்டாளிகள் (₹25K+ அடுக்குகள்)',
                foodTitle: 'உடனடி வாழ்க்கை முறை & உணவு வவுச்சர்கள்',
                loginTitle: 'ஒப்பந்தக்காரர் பாதுகாப்பான நோடு உள்நுழைவு',
                loginPlaceholder: 'மொபைல் எண்ணை உள்ளிடவும்',
                loginBtn: 'உள்நுழைக',
                wa: [
                    "🚀 மாட்ஜினு வெப்3 டெக்னாலஜிஸில் இணையுங்கள்! அரசு அங்கீகரிக்கப்பட்ட கிளவுட் கம்ப்யூட் மற்றும் 24K தங்க பரிசுப் பொருட்கள்: ",
                    "💼 சவரன் கிளவுட் & 24K தங்க ஷோரூம் வவுச்சர்களில் முதலீடு செய்யுங்கள் (Tanishq/GRT). இன்று தொடங்குங்கள்: ",
                    "🏆 தினசரி இ-காமர்ஸ் பணிகளை முடித்து தினசரி பணம் பெறுங்கள்! இங்கே இணையுங்கள்: ",
                    "🌟 மீட்டி (MeitY) அங்கீகரிக்கப்பட்ட ஸ்டார்ட்அப் நிறுவனம் வழங்கும் சர்வர் நோடுகள்: ",
                    "💰 மாட்ஜினு வெப்3 உடன் உங்களது டிஜிட்டல் சொத்து போர்ட்ஃபோலியோவை உருவாக்குங்கள்: ",
                    "💎 24K தங்க ஷோரூம் பார்ட்னர்களை அன்லாக் செய்து தினசரி பணி வருமானம் பெறுங்கள்: ",
                    "🔒 பாதுகாப்பான என்டர்பிரைஸ் டெர்மினல் மற்றும் தானியங்கி சரிபார்ப்பு நெட்வொர்க்: ",
                    "🎁 10%-12% ரெஃபரல் போனஸ் மற்றும் தினசரி பணிப் பலன்களைப் பெறுங்கள்: ",
                    "🤖 மாட்ஜினு ஏஐ ஸ்டுடியோ & கிளவுட் நெட்வொர்க் மூலம் தன்னாட்சி பணிகளை அனுபவியுங்கள்: ",
                    "📈 14 நாள் சர்வர் நோடு உரிமைகளுடன் உங்கள் வருமானத்தை உயர்த்துங்கள்: "
                ]
            },
            'TE': {
                badge: "👑 భారతదేశపు మొదటి స్వయంప్రతిపత్తి కలిగిన AI స్టూడియో",
                title: 'సావరీన్ క్లౌడ్ కంప్యూట్ &<br><span>ఆటోనమస్ జాబ్‌వర్క్స్ & లైవ్ గోల్డ్ వాల్ట్</span>',
                desc: 'మాడ్జినూ వెబ్3 టెక్నాలజీస్ ప్రభుత్వ గుర్తింపు పొందిన స్టార్టప్.',
                launchBtn: 'సెక్యూర్ ఎంటర్‌ప్రైజ్ టెర్మినల్‌ను ప్రారంభించండి',
                featTitle: 'ప్లాట్‌ఫారమ్ ఎకోసిస్టమ్ ఫీచర్లు',
                feat1: 'ఉచిత టైర్: మొబైల్ నంబర్‌కు 4 రోజులు రోజువారీ ₹25 సంపాదించండి (మొత్తం ₹100, కనిష్ట ఉపసంహరణ ₹100).',
                feat2: 'సర్వర్ ప్యాకేజీలు: ₹2,000 నుండి ₹1,00,000 వరకు టైర్లు (+18% GST) 14 రోజుల చక్రంతో.',
                feat3: '3-టైర్ రెఫరల్: సిల్వర్ (10%) → గోల్డ్ (12%) → డైమండ్ (15%) తక్షణ కమిషన్.',
                waTitle: '10 ప్రత్యేకమైన వాట్సాప్ రెఫరల్ స్క్రిప్ట్‌లు',
                waDesc: 'ఆటో-ఎంబెడెడ్ ఐడీతో మీ రెఫరల్ లింక్‌ను షేర్ చేయండి:',
                partnerTitle: 'మద్దతు ఉన్న వోచర్ & రివార్డ్ భాగస్వాములు',
                partnerSub: '* ఎంటర్‌ప్రైజ్ రివార్డ్ పార్ట్‌నర్స్ (API ఇంటిగ్రేషన్ త్వరలో రానుంది)',
                goldTitle: '24K గోల్డ్ షోరూమ్ భాగస్వాములు (₹25K+ టైర్లు)',
                foodTitle: 'తక్షణ జీవనశైలి & ఆహార వోచర్లు',
                loginTitle: 'కాంట్రాక్టర్ సెక్యూర్ నోడ్ లాగిన్',
                loginPlaceholder: 'మొబైల్ నంబర్‌ను నమోదు చేయండి',
                loginBtn: 'లాగిన్',
                wa: [
                    "🚀 మాడ్జినూ వెబ్3 టెక్నాలజీస్‌లో చేరండి - ప్రభుత్వ గుర్తింపు పొందిన క్లౌడ్ కంప్యూట్ & గోల్డ్ వాల్ట్ రివార్డ్స్: ",
                    "💎 సావరీన్ క్లౌడ్ & 24K గోల్డ్ షోరూమ్ వోచర్లలో పెట్టుబడి పెట్టండి (Tanishq/GRT): ",
                    "💼 రోజువారీ ఇ-కామర్స్ జాబ్‌వర్క్స్ పూర్తి చేసి రోజువారీ పేఅవుట్లు పొందండి: ",
                    "🌟 MeitY గుర్తించిన స్టార్టప్ హై-త్రూపుట్ సర్వర్ నోడ్స్ & రివార్డ్స్ అందిస్తోంది: ",
                    "💰 మాడ్జినూ వెబ్3తో మీ సురక్షిత డిజిటల్ అసెట్ పోర్ట్‌ఫోలియోను నిర్మించండి: ",
                    "🏆 24K గోల్డ్ షోరూమ్ భాగస్వాములను అన్‌లాక్ చేయండి & రోజువారీ ఆదాయం పొందండి: ",
                    "🔒 సురక్షిత ఎంటర్‌ప్రైజ్ టెర్మినల్ & ఆటోమేటెడ్ వెరిఫికేషన్ పైప్‌లైన్స్: ",
                    "🎁 10%-12% రెఫరల్ బోనస్‌లు & రోజువారీ టాస్క్ పేఅవుట్లు పొందండి: ",
                    "🤖 మాడ్జినూ AI స్టూడియో & క్లౌడ్ నెట్‌వర్క్ ద్వారా శక్తివంతమైన ఆటోనమస్ జాబ్‌వర్క్స్: ",
                    "📈 14-రోజుల సర్వర్ నోడ్ లైసెన్స్‌లతో మీ ఆదాయాన్ని పెంచుకోండి: "
                ]
            },
            'KN': {
                badge: "👑 ಭಾರತದ ಮೊದಲ ಸ್ವಾಯತ್ತ AI ಸ್ಟುಡಿಯೋ",
                title: 'ಸವರನ್ ಕ್ಲೌಡ್ ಕಂಪ್ಯೂಟ್ &<br><span>ಸ್ವಾಯತ್ತ ಉದ್ಯೋಗಗಳು & ಲೈವ್ ಗೋಲ್ಡ್ ವಾಲ್ಟ್</span>',
                desc: 'ಮಾಡ್ಜಿನು ವೆಬ್3 ಟೆಕ್ನಾಲಜೀಸ್ ಭಾರತ ಸರ್ಕಾರದ ಗುರುತಿಸಲ್ಪಟ್ಟ ಸ್ಟಾರ್ಟಪ್.',
                launchBtn: 'ಸುರಕ್ಷಿತ ಎಂಟರ್‌ಪ್ರೈಸ್ ಟರ್ಮಿನಲ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ',
                featTitle: 'ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಪರಿಸರ ವ್ಯವಸ್ಥೆಯ ವೈಶಿಷ್ಟ್ಯಗಳು',
                feat1: 'ಉಚಿತ ಶ್ರೇಣಿ: ಪ್ರತಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ 4 ದಿನಗಳವರೆಗೆ ಪ್ರತಿದಿನ ₹25 ಗಳಿಸಿ (ಒಟ್ಟು ₹100, ಕನಿಷ್ಠ ಹಿಂತೆಗೆದುಕೊಳ್ಳುವಿಕೆ ₹100).',
                feat2: 'ಸರ್ವರ್ ಪ್ಯಾಕೇಜುಗಳು: ₹2,000 ರಿಂದ ₹1,00,000 ವರೆಗಿನ ಶ್ರೇಣಿಗಳು (+18% ಜಿಎಸ್‌ಟಿ).',
                feat3: '3-ಶ್ರೇಣಿಯ ರೆಫರಲ್: ಬೆಳ್ಳಿ (10%) → ಚಿನ್ನ (12%) → ವಜ್ರ (15%) ತಕ್ಷಣದ ಕಮಿಷನ್.',
                waTitle: '10 ಅನನ್ಯ ವಾಟ್ಸಾಪ್ ರೆಫರಲ್ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು',
                waDesc: 'ನಿಮ್ಮ ರೆಫರಲ್ ಲಿಂಕ್ ಅನ್ನು ಹಂಚಿಕೊಳ್ಳಿ:',
                partnerTitle: 'ಬೆಂಬಲಿತ ವೋಚರ್ ಮತ್ತು ರಿವಾರ್ಡ್ ಪಾಲುದಾರರು',
                partnerSub: '* ಎಂಟರ್‌ಪ್ರೈಸ್ ರಿವಾರ್ಡ್ ಪಾಲುದಾರರು (ಶೀಘ್ರದಲ್ಲೇ ಬರಲಿದೆ)',
                goldTitle: '24K ಗೋಲ್ಡ್ ಶೋರೂಮ್ ಪಾಲುದಾರರು (₹25K+ ಶ್ರೇಣಿಗಳು)',
                foodTitle: 'ತ್ವರಿತ ಜೀವನಶೈಲಿ ಮತ್ತು ಆಹಾರ ವೋಚರ್‌ಗಳು',
                loginTitle: 'ಕಂಟ್ರಾಕ್ಟರ್ ಸುರಕ್ಷಿತ ನೋಡ್ ಲಾಗಿನ್',
                loginPlaceholder: 'ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ',
                loginBtn: 'ಲಾಗಿನ್',
                wa: [
                    "🚀 ಮಾಡ್ಜಿನು ವೆಬ್3 ಟೆಕ್ನಾಲಜೀಸ್‌ಗೆ ಸೇರಿ - ಸರ್ಕಾರಿ ಗುರುತಿಸಲ್ಪಟ್ಟ ಕ್ಲೌಡ್ ಕಂಪ್ಯೂಟ್ & ಗೋಲ್ಡ್ ರಿವಾರ್ಡ್ಸ್: ",
                    "💎 ಸವರನ್ ಕ್ಲೌಡ್ & 24K ಗೋಲ್ಡ್ ಶೋರೂಮ್ ವೋಚರ್‌ಗಳಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡಿ (Tanishq/GRT): ",
                    "💼 ದೈನಂದಿನ ಇ-ಕಾಮರ್ಸ್ ಕೆಲಸಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ ಮತ್ತು ದೈನಂದಿನ ಪಾವತಿಗಳನ್ನು ಗಳಿಸಿ: ",
                    "🌟 MeitY ಗುರುತಿಸಲ್ಪಟ್ಟ ಸ್ಟಾರ್ಟಪ್‌ನೊಂದಿಗೆ ಹೈ-ಥ್ರೂಪುಟ್ ಸರ್ವರ್ ನೋಡ್‌ಗಳನ್ನು ಪಡೆಯಿರಿ: ",
                    "💰 ಮಾಡ್ಜಿನು ವೆಬ್3 ಜೊತೆಗೆ ನಿಮ್ಮ ಸುರಕ್ಷಿತ ಡಿಜಿಟಲ್ ಆಸ್ತಿ ಪೋರ್ಟ್‌ಫೋಲಿಯೊ ನಿರ್ಮಿಸಿ: ",
                    "🏆 24K ಗೋಲ್ಡ್ ಶೋರೂಮ್ ಪಾಲುದಾರರನ್ನು ಅನ್ಲಾಕ್ ಮಾಡಿ ಮತ್ತು ದೈನಂದಿನ ಆದಾಯ ಗಳಿಸಿ: ",
                    "🔒 ಸುರಕ್ಷಿತ ಎಂಟರ್‌ಪ್ರೈಸ್ ಟರ್ಮಿನಲ್ ಮತ್ತು ಸ್ವಯಂಚಾಲಿತ ಪರಿಶೀಲನಾ管道: ",
                    "🎁 10%-12% ರೆಫರಲ್ ಬೋನಸ್‌ಗಳು ಮತ್ತು ದೈನಂದಿನ ಕಾರ್ಯ ಪಾವತಿಗಳನ್ನು ಪಡೆಯಿರಿ: ",
                    "🤖 ಮಾಡ್ಜಿನು AI ಸ್ಟುಡಿಯೋ ಮತ್ತು ಕ್ಲೌಡ್ ನೆಟ್‌ವರ್ಕ್‌ನಿಂದ ಶಕ್ತಿಪಡೆದ ಸ್ವಾಯತ್ತ ಕೆಲಸಗಳು: ",
                    "📈 14 ದಿನಗಳ ಸರ್ವರ್ ನೋಡ್ ಪರವಾನಗಿಗಳೊಂದಿಗೆ ನಿಮ್ಮ ಗಳಿಕೆಯನ್ನು ಹೆಚ್ಚಿಸಿ: "
                ]
            },
            'ML': {
                badge: "👑 ഇന്ത്യയിലെ ആദ്യത്തെ സ്വയംഭരണ AI സ്റ്റുഡിയോ",
                title: 'സവറൻ ക്ലൗഡ് കമ്പ്യൂട്ട് &<br><span>ഓട്ടോണമസ് ജോബ്‌വർക്സ് & ലൈവ് ഗോൾഡ് വാൾട്ട്</span>',
                desc: 'മാഡ്ജിനു വെബ്3 ടെക്നോളജീസ് MeitY അംഗീകൃത സ്റ്റാർട്ടപ്പാണ്.',
                launchBtn: 'സുരക്ഷിത എൻ്റർപ്രൈസ് ടെർമിനൽ സമാരംഭിക്കുക',
                featTitle: 'പ്ലാറ്റ്‌ഫോം ഇക്കോസിസ്റ്റം സവിശേഷതകൾ',
                feat1: 'സൗജന്യ ടയർ: ഒരു മൊബൈൽ നമ്പറിന് 4 ദിവസത്തേക്ക് ദിവസേന ₹25 നേടുക (ആകെ ₹100, മിനിമം പിൻവലിക്കൽ ₹100).',
                feat2: 'സർവർ പാക്കേജുകൾ: ₹2,000 മുതൽ ₹1,00,000 വരെ (+18% ജിഎസ്ടി).',
                feat3: '3-ടയർ റഫറൽ: വെള്ളി (10%) → സ്വർണ്ണം (12%) → ഡയമണ്ട് (15%).',
                waTitle: '10 അതുത്പന്ന വാട്ട്സാപ്പ് റഫറൽ സ്ക്രിപ്റ്റുകൾ',
                waDesc: 'നിങ്ങളുടെ റഫറൽ ലിങ്ക് പങ്കിടുക:',
                partnerTitle: 'പിന്തുണയ്ക്കുന്ന വൗച്ചറും റിവാർഡ് പങ്കാളികളും',
                partnerSub: '* എൻ്റർപ്രൈസ് റിവാർഡ് പങ്കാളികൾ (ഉടൻ വരുന്നു)',
                goldTitle: '24K ഗോൾഡ് ഷോറൂം പങ്കാളികൾ (₹25K+ ടയറുകൾ)',
                foodTitle: 'തൽക്ഷണ ലൈഫ്‌സ്റ്റൈൽ & ഫുഡ് വൗച്ചറുകൾ',
                loginTitle: 'കൺട്രാക്ടർ സുരക്ഷിത നോഡ് ലോഗിൻ',
                loginPlaceholder: 'മൊബൈൽ നമ്പർ നൽകുക',
                loginBtn: 'ലോഗിൻ',
                wa: [
                    "🚀 മാഡ്ജിനു വെബ്3 ടെക്നോളജീസിൽ ചേരൂ - സർക്കാർ അംഗീകൃത ക്ലൗഡ് കമ്പ്യൂട്ട് & ഗോൾഡ് റിവാർഡുകൾ: ",
                    "💎 സവറൻ ക്ലൗഡ് & 24K ഗോൾഡ് ഷോറൂം വൗച്ചറുകളിൽ നിക്ഷേപിക്കൂ (Tanishq/GRT): ",
                    "💼 ദിവസേനയുള്ള ഇ-കോമേഴ്സ് ജോലികൾ പൂർത്തിയാക്കി പ്രതിദിന പേഔട്ടുകൾ നേടൂ: ",
                    "🌟 MeitY അംഗീകൃത സ്റ്റാർട്ടപ്പ് നൽകുന്ന ഹൈ-ത്രുപുട്ട് സർവർ നോഡുകൾ: ",
                    "💰 മാഡ്ജിനു വെബ്3 ഉപയോഗിച്ച് നിങ്ങളുടെ സുരക്ഷിത ഡിജിറ്റൽ അസറ്റ് പോർട്ട്ഫോളിയോ നിർമ്മിക്കൂ: ",
                    "🏆 24K ഗോൾഡ് ഷോറൂം പങ്കാളികളെ അൺലോക്ക് ചെയ്ത് പ്രതിദിന വരുമാനം നേടൂ: ",
                    "🔒 സുരക്ഷിത എൻ്റർപ്രൈസ് ടർമിനലും ഓട്ടോമേറ്റഡ് വെരിഫിക്കേഷൻ പൈപ്പ്‌ലൈനുകളും: ",
                    "🎁 10%-12% റഫറൽ ബോണസും പ്രതിദിന ടാസ്ക് പേഔട്ടുകളും സ്വന്തമാക്കൂ: ",
                    "🤖 മാഡ്ജിനു AI സ്റ്റുഡിയോ & ക്ലൗഡ് നെറ്റ്‌വർക്ക് നൽകുന്ന ഓട്ടോണമസ് ജോബ്‌വർക്സ്: ",
                    "📈 14 ദിവസത്തെ സർവർ നോഡ് ലൈസൻസുകൾ വഴി നിങ്ങളുടെ വരുമാനം വർദ്ധിപ്പിക്കൂ: "
                ]
            },
            'HI': {
                badge: "👑 भारत का पहला स्वायत्त एआई स्टूडियो",
                title: 'सोवरेइन क्लाउड कंप्यूट और<br><span>ऑटोनॉमस जॉबवर्क्स और लाइव गोल्ड वॉल्ट</span>',
                desc: 'माड्जिनू वेब3 टेक्नोलॉजीज MeitY के तहत मान्यता प्राप्त स्टार्टअप है।',
                launchBtn: 'सुरक्षित एंटरप्राइज टर्मिनल लॉन्च करें',
                featTitle: 'प्लेटफ़ॉर्म पारिस्थितिकी तंत्र सुविधाएँ',
                feat1: 'फ्री टियर: प्रति मोबाइल नंबर 4 दिनों के लिए प्रतिदिन ₹25 कमाएं (कुल ₹100, न्यूनतम निकासी ₹100)।',
                feat2: 'सर्वर पैकेज: ₹2,000 से ₹1,00,000 तक के टियर (+18% जीएसटी)।',
                feat3: '3-टियर रेफ़रल: सिल्वर (10%) → गोल्ड (12%) → डायमंड (15%) तत्काल कमीशन।',
                waTitle: '10 अद्वितीय व्हाट्सएप रेफ़रल स्क्रिप्ट',
                waDesc: 'ऑटो-एम्बेडेड आईडी के साथ अपना रेफ़रल लिंक साझा करें:',
                partnerTitle: 'समर्थित वाउचर और पुरस्कार भागीदार',
                partnerSub: '* एंटरप्राइज़ रिवार्ड पार्टनर (जल्द ही आ रहा है)',
                goldTitle: '24K गोल्ड शोरूम पार्टनर (₹25K+ टियर)',
                foodTitle: 'त्वरित जीवन शैली और खाद्य वाउचर',
                loginTitle: 'कॉन्ट्रैक्टर सुरक्षित नोड लॉगिन',
                loginPlaceholder: 'मोबाइल नंबर दर्ज करें',
                loginBtn: 'लॉगिन',
                wa: [
                    "🚀 माड्जिनू वेब3 टेक्नोलॉजीज से जुड़ें - सरकार द्वारा मान्यता प्राप्त क्लाउड कंप्यूट और गोल्ड वॉल्ट पुरस्कार: ",
                    "💎 सोवरेइन क्लाउड और 24K गोल्ड शोरूम वाउचर में निवेश करें (Tanishq/GRT): ",
                    "💼 दैनिक ई-कॉमर्स जॉबवर्क पूरा करें और रोजाना भुगतान प्राप्त करें: ",
                    "🌟 MeitY मान्यता प्राप्त स्टार्टअप द्वारा उच्च-थ्रूपुट सर्वर नोड्स और पुरस्कार: ",
                    "💰 माड्जिनू वेब3 के साथ अपना सुरक्षित डिजिटल संपत्ति पोर्टफोलियो बनाएं: ",
                    "🏆 24K गोल्ड शोरूम भागीदारों को अनलॉक करें और दैनिक कार्य आय सुरक्षित करें: ",
                    "🔒 सुरक्षित एंटरप्राइज़ टर्मिनल और स्वचालित सत्यापन पाइपलाइन: ",
                    "🎁 10%-12% रेफरल बोनस और दैनिक कार्य भुगतान प्राप्त करें: ",
                    "🤖 माड्जिनू एआई स्टूडियो और क्लाउड नेटवर्क द्वारा संचालित ऑटोनॉमस जॉबवर्क्स: ",
                    "📈 14-दिवसीय सर्वर नोड लाइसेंस के साथ अपनी कमाई बढ़ाएं: "
                ]
            },
            'MR': {
                badge: "👑 भारताचे पहिले स्वायत्त AI स्टुडिओ",
                title: 'सोव्हरेईन क्लाउड कॉम्प्युट आणि<br><span>ऑटोनॉमस जॉबवर्क्स आणि लाइव्ह गोल्ड वॉल्ट</span>',
                desc: 'माड्झिनू वेब3 टेक्नॉलॉजीज ही मान्यताप्राप्त स्टार्टअप आहे.',
                launchBtn: 'सुरक्षित एंटरप्राइझ टर्मिनल सुरू करा',
                featTitle: 'प्लॅटफॉर्म इकोसिस्टम वैशिष्ट्ये',
                feat1: 'फ्री टियर: प्रति मोबाईल नंबर 4 दिवस दररोज ₹25 कमवा (एकूण ₹100, किमान काढणे ₹100).',
                feat2: 'सर्व्हर पॅकेजेस: ₹2,000 ते ₹1,00,000 पर्यंतचे स्तर (+18% जीएसटी).',
                feat3: '3-स्तरीय संदर्भ: सिल्व्हर (10%) → गोल्ड (12%) → डायमंड (15%).',
                waTitle: '10 अद्वितीय WhatsApp संदर्भ स्क्रिप्ट्स',
                waDesc: 'तुमची संदर्भ लिंक शेअर करा:',
                partnerTitle: 'समर्थित व्हाउचर आणि बक्षीस भागीदार',
                partnerSub: '* एंटरप्राइझ रिवॉर्ड पार्टनर (लवकरच येत आहे)',
                goldTitle: '24K गोल्ड शोरूम भागीदार (₹25K+ स्तर)',
                foodTitle: 'झटपट जीवनशैली आणि अन्न व्हाउचर',
                loginTitle: 'कंट्रॅक्टर सुरक्षित नोड लॉगिन',
                loginPlaceholder: 'मोबाईल नंबर प्रविष्ट करा',
                loginBtn: 'लॉगिन',
                wa: [
                    "🚀 माड्झिनू वेब3 टेक्नॉलॉजीजमध्ये सामील व्हा - सरकार मान्यताप्राप्त क्लाउड कॉम्प्युट आणि गोल्ड वॉल्ट बक्षिसे: ",
                    "💎 सोव्हरेईन क्लाउड आणि 24K गोल्ड शोरूम व्हाउचरमध्ये गुंतवणूक करा (Tanishq/GRT): ",
                    "💼 दैनिक ई-कॉमर्स कार्ये पूर्ण करा आणि दररोज पैसे मिळवा: ",
                    "🌟 MeitY मान्यताप्राप्त स्टार्टअप कडून हाय-थ्रूपुट सर्व्हर नोड्स आणि बक्षिसे: ",
                    "💰 माड्झिनू वेब3 सह तुमचे सुरक्षित डिजिटल मालमत्ता पोर्टफोलिओ तयार करा: ",
                    "🏆 24K गोल्ड शोरूम भागीदारांना अनलॉक करा आणि दैनिक उत्पन्न सुरक्षित करा: ",
                    "🔒 सुरक्षित एंटरप्राइझ टर्मिनल आणि स्वयंचलित पडताळणी पाइपलाइन: ",
                    "🎁 10%-12% रेफरल बोनस आणि दैनिक कार्य पेआउट्स मिळवा: ",
                    "🤖 माड्झिनू AI स्टुडिओ आणि क्लाउड नेटवर्क द्वारे ऑटोनॉमस जॉबवर्क्सचा अनुभव घ्या: ",
                    "📈 14-दिवसीय सर्व्हर परवान्यांसह तुमची कमाई वाढवा: "
                ]
            }
        };

        function changeLanguage() {
            const lang = document.getElementById('langSelector').value;
            const t = translations[lang] || translations['EN'];
            
            // Hero section
            document.getElementById('hero-badge').innerText = t.badge;
            document.getElementById('hero-title').innerHTML = t.title;
            document.getElementById('hero-desc').innerText = t.desc;
            
            // Launch button
            const btnPrimary = document.querySelector('.btn-primary');
            if(btnPrimary) btnPrimary.innerHTML = '<i class="fa-solid fa-arrow-right-to-bracket"></i> ' + t.launchBtn;

            // Ecosystem Features
            const featTitle = document.getElementById('feat-title');
            if(featTitle) featTitle.innerHTML = '<i class="fa-solid fa-list-check"></i> ' + t.featTitle;
            
            const featList = document.querySelectorAll('#feat-box ul li');
            if(featList.length >= 3) {
                featList[0].innerHTML = '<strong>' + t.feat1.split(':')[0] + ':</strong>' + t.feat1.split(':')[1];
                featList[1].innerHTML = '<strong>' + t.feat2.split(':')[0] + ':</strong>' + t.feat2.split(':')[1];
                featList[2].innerHTML = '<strong>' + t.feat3.split(':')[0] + ':</strong>' + t.feat3.split(':')[1];
            }

            // WhatsApp scripts section
            const waHeader = document.querySelector('.section-box h3');
            if(waHeader && waHeader.innerText.includes('WhatsApp')) {
                waHeader.innerHTML = '<i class="fa-brands fa-whatsapp"></i> ' + t.waTitle;
            }
            const waDesc = document.querySelector('.section-box p');
            if(waDesc && waDesc.innerText.includes('referral link')) {
                waDesc.innerText = t.waDesc;
            }

            // Partner section headers
            const partnerHeaders = document.querySelectorAll('.section-box');
            partnerHeaders.forEach(box => {
                if(box.innerHTML.includes('Supported Voucher')) {
                    const titleEl = box.querySelector('div[style*="font-weight: bold"]');
                    if(titleEl) titleEl.innerHTML = '<i class="fa-solid fa-ticket"></i> ' + t.partnerTitle;
                    const subEl = box.querySelector('div[style*="color: #34d399"]');
                    if(subEl) subEl.innerText = t.partnerSub;
                    
                    const goldEl = box.querySelector('div[style*="color: #f59e0b"]');
                    if(goldEl) goldEl.innerHTML = '<i class="fa-solid fa-crown"></i> ' + t.goldTitle;

                    const foodEl = box.querySelector('div[style*="color: #38bdf8; margin-bottom: 8px"]');
                    if(foodEl) foodEl.innerHTML = '<i class="fa-solid fa-utensils"></i> ' + t.foodTitle;
                }
                if(box.id === 'login-section') {
                    const loginH3 = box.querySelector('h3');
                    if(loginH3) loginH3.innerHTML = '<i class="fa-solid fa-shield-keyhole"></i> ' + t.loginTitle;
                    const inputEl = document.getElementById('login-mobile');
                    if(inputEl) inputEl.placeholder = t.loginPlaceholder;
                    const loginBtn = box.querySelector('button');
                    if(loginBtn) loginBtn.innerText = t.loginBtn;
                }
            });
        }
    </script>
"""

# Replace script section in file
if "<script>" in code:
    code = code.split("<script>")[0] + new_js

with open("index.html", "w") as f:
    f.write(code)

print("Full multi-language translation injection complete!")
