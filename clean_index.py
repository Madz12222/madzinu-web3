with open("index.html", "r") as f:
    html = f.read()

# Remove any accidental trailing code leakage if present
if "function renderDashboard" in html:
    # Split at the first appearance of the raw script text in body and keep clean HTML
    parts = html.split("function renderDashboard")
    html = parts[0]

# Now append the correct, clean script block properly enclosed
clean_script = """    <script>
        const translations = {
            'EN': {
                badge: "👑 INDIA'S FIRST AUTONOMOUS AI STUDIO & CLOUD NETWORK",
                title: 'Sovereign Cloud Compute &<br><span>Autonomous Jobworks & Live Gold Vault</span>',
                desc: 'Madzinu Web3 Technologies is a Govt. of India Recognized Startup entity under MeitY with approved IndiaAI Portal compute access. Provision high-throughput server compute packages from ₹2,000 to ₹1,00,000.',
                ecoTitle: 'Platform Ecosystem Features',
                eco1Lbl: 'Free Tier:',
                eco1Txt: ' Earn ₹25 daily for 4 days per mobile number (Total ₹100, Min Withdraw ₹100).',
                eco2Lbl: 'Server Packages:',
                eco2Txt: ' Tiers ranging from ₹2,000 to ₹1,00,000 (+18% GST) with 14-day cycle.',
                eco3Lbl: '3-Tier Referral:',
                eco3Txt: ' Silver (10%) → Gold (12%) → Diamond (15%) instant commission.',
                waTitle: '10 Unique WhatsApp Referral Scripts',
                waDesc: 'Share your referral link with auto-embedded ID:',
                partnerTitle: 'Supported Voucher & Reward Partners',
                goldTitle: '24K GOLD SHOWROOM PARTNERS (ENTERPRISE TIERS ₹25K+)',
                foodTitle: 'INSTANT LIFESTYLE & FOOD VOUCHERS',
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
                ecoTitle: 'பிளாட்ஃபார்ம் சுற்றுச்சூழல் அம்சங்கள்',
                eco1Lbl: 'இலவச அடுக்கு:',
                eco1Txt: ' மொபைல் எண்ணுக்கு 4 நாட்களுக்கு தினமும் ₹25 சம்பாதிக்கவும் (மொத்தம் ₹100, குறைந்தபட்ச திரும்பப் பெறுதல் ₹100).',
                eco2Lbl: 'சர்வர் தொகுப்புகள்:',
                eco2Txt: ' ₹2,000 முதல் ₹1,00,000 வரையிலான அடுக்குகள் (+18% ஜிஎஸ்டி) 14 நாள் சுழற்சியுடன்.',
                eco3Lbl: '3-அடுக்கு பரிந்துரை:',
                eco3Txt: ' வெள்ளி (10%) → தங்கம் (12%) → வைரம் (15%) உடனடி கமிஷன்.',
                waTitle: '10 தனித்துவமான வாட்ஸ்அப் பரிந்துரை ஸ்கிரிப்டுகள்',
                waDesc: 'தானியங்கி ஐடியுடன் உங்கள் பரிந்துரை இணைப்பைப் பகிரவும்:',
                partnerTitle: 'ஆதரிக்கப்படும் வவுச்சர் மற்றும் வெகுமதி கூட்டாளிகள்',
                goldTitle: '24K தங்க ஷோரூம் கூட்டாளிகள் (₹25K+ அடுக்குகள்)',
                foodTitle: 'உடனடி வாழ்க்கை முறை & உணவு வவுச்சர்கள்',
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
                ecoTitle: 'ప్లాట్‌ఫారమ్ ఎకోసిస్టమ్ ఫీచర్లు',
                eco1Lbl: 'ఉచిత టైర్:',
                eco1Txt: ' మొబైల్ నంబర్‌కు 4 రోజులు రోజువారీ ₹25 సంపాదించండి (మొత్తం ₹100, కనిష్ట ఉపసంహరణ ₹100).',
                eco2Lbl: 'సర్వర్ ప్యాకేజీలు:',
                eco2Txt: ' ₹2,000 నుండి ₹1,00,000 వరకు టైర్లు (+18% GST) 14 రోజుల చక్రంతో.',
                eco3Lbl: '3-టైర్ రెఫరల్:',
                eco3Txt: ' సిల్వర్ (10%) → గోల్డ్ (12%) → డైమండ్ (15%) తక్షణ కమిషన్.',
                waTitle: '10 ప్రత్యేకమైన వాట్సాప్ రెఫరల్ స్క్రిప్ట్‌లు',
                waDesc: 'ఆటో-ఎంబెడెడ్ ఐడీతో మీ రెఫరల్ లింక్‌ను షేర్ చేయండి:',
                partnerTitle: 'మద్దతు ఉన్న వోచర్ & రివార్డ్ భాగస్వాములు',
                goldTitle: '24K గోల్డ్ షోరూమ్ భాగస్వాములు (₹25K+ టైర్లు)',
                foodTitle: 'తక్షణ జీవనశైలి & ఆహార వోచర్లు',
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
                ecoTitle: 'ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಪರಿಸರ ವ್ಯವಸ್ಥೆಯ ವೈಶಿಷ್ಟ್ಯಗಳು',
                eco1Lbl: 'ಉಚಿತ ಶ್ರೇಣಿ:',
                eco1Txt: ' ಪ್ರತಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ 4 ದಿನಗಳವರೆಗೆ ಪ್ರತಿದಿನ ₹25 ಗಳಿಸಿ (ಒಟ್ಟು ₹100, ಕನಿಷ್ಠ ಹಿಂತೆಗೆದುಕೊಳ್ಳುವಿಕೆ ₹100).',
                eco2Lbl: 'ಸರ್ವರ್ ಪ್ಯಾಕೇಜುಗಳು:',
                eco2Txt: ' ₹2,000 ರಿಂದ ₹1,00,000 ವರೆಗಿನ ಶ್ರೇಣಿಗಳು (+18% ಜಿಎಸ್‌ಟಿ).',
                eco3Lbl: '3-ಶ್ರೇಣಿಯ ರೆಫರಲ್:',
                eco3Txt: ' ಬೆಳ್ಳಿ (10%) → ಚಿನ್ನ (12%) → ವಜ್ರ (15%) ತಕ್ಷಣದ ಕಮಿಷನ್.',
                waTitle: '10 ಅನನ್ಯ ವಾಟ್ಸಾಪ್ ರೆಫರಲ್ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು',
                waDesc: 'ನಿಮ್ಮ ರೆಫರಲ್ ಲಿಂಕ್ ಅನ್ನು ಹಂಚಿಕೊಳ್ಳಿ:',
                partnerTitle: 'ಬೆಂಬಲಿತ ವೋಚರ್ ಮತ್ತು ರಿವಾರ್ಡ್ ಪಾಲುದಾರರು',
                goldTitle: '24K ಗೋಲ್ಡ್ ಶೋರೂಮ್ ಪಾಲುದಾರರು (₹25K+ ಶ್ರೇಣಿಗಳು)',
                foodTitle: 'ತ್ವರಿತ ಜೀವನಶೈಲಿ ಮತ್ತು ಆಹಾರ ವೋಚರ್‌ಗಳು',
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
                ecoTitle: 'പ്ലാറ്റ്‌ഫോം ഇക്കോസിസ്റ്റം സവിശേഷതകൾ',
                eco1Lbl: 'സൗജന്യ ടയർ:',
                eco1Txt: ' ഒരു മൊബൈൽ നമ്പറിന് 4 ദിവസത്തേക്ക് ദിവസേന ₹25 നേടുക (ആകെ ₹100, മിനിമം പിൻവലിക്കൽ ₹100).',
                eco2Lbl: 'സർവർ പാക്കേജുകൾ:',
                eco2Txt: ' ₹2,000 മുതൽ ₹1,00,000 വരെ (+18% ജിഎസ്ടി).',
                eco3Lbl: '3-ടയർ റഫറൽ:',
                eco3Txt: ' വെള്ളി (10%) → സ്വർണ്ണം (12%) → ഡയമണ്ട് (15%).',
                waTitle: '10 അതുത്പന്ന വാട്ട്സാപ്പ് റഫറൽ സ്ക്രിപ്റ്റുകൾ',
                waDesc: 'നിങ്ങളുടെ റഫറൽ ലിങ്ക് പങ്കിടുക:',
                partnerTitle: 'പിന്തുണയ്ക്കുന്ന വൗച്ചറും റിവാർഡ് പങ്കാളികളും',
                goldTitle: '24K ഗോൾഡ് ഷോറൂം പങ്കാളികൾ (₹25K+ ടയറുകൾ)',
                foodTitle: 'തൽക്ഷണ ലൈഫ്‌സ്റ്റൈൽ & ഫുഡ് വൗച്ചറുകൾ',
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
                ecoTitle: 'प्लेटफ़ॉर्म पारिस्थितिकी तंत्र सुविधाएँ',
                eco1Lbl: 'फ्री टियर:',
                eco1Txt: ' प्रति मोबाइल नंबर 4 दिनों के लिए प्रतिदिन ₹25 कमाएं (कुल ₹100, न्यूनतम निकासी ₹100)।',
                eco2Lbl: 'सर्वर पैकेज:',
                eco2Txt: ' ₹2,000 से ₹1,00,000 तक के टियर (+18% जीएसटी)।',
                eco3Lbl: '3-टियर रेफ़रल:',
                eco3Txt: ' सिल्वर (10%) → गोल्ड (12%) → डायमंड (15%) तत्काल कमीशन।',
                waTitle: '10 अद्वितीय व्हाट्सएप रेफ़रल स्क्रिप्ट',
                waDesc: 'ऑटो-एम्बेडेड आईडी के साथ अपना रेफ़रल लिंक साझा करें:',
                partnerTitle: 'समर्थित वाउचर और पुरस्कार भागीदार',
                goldTitle: '24K गोल्ड शोरूम पार्टनर (₹25K+ टियर)',
                foodTitle: 'त्वरित जीवन शैली और खाद्य वाउचर',
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
                ecoTitle: 'प्लॅटफॉर्म इकोसिस्टम वैशिष्ट्ये',
                eco1Lbl: 'फ्री टियर:',
                eco1Txt: ' प्रति मोबाईल नंबर 4 दिवस दररोज ₹25 कमवा (एकूण ₹100, किमान काढणे ₹100).',
                eco2Lbl: 'सर्व्हर पॅकेजेस:',
                eco2Txt: ' ₹2,000 ते ₹1,00,000 पर्यंतचे स्तर (+18% जीएसटी).',
                eco3Lbl: '3-स्तरीय संदर्भ:',
                eco3Txt: ' सिल्व्हर (10%) → गोल्ड (12%) → डायमंड (15%).',
                waTitle: '10 अद्वितीय WhatsApp संदर्भ स्क्रिप्ट्स',
                waDesc: 'तुमची संदर्भ लिंक शेअर करा:',
                partnerTitle: 'समर्थित व्हाउचर आणि बक्षीस भागीदार',
                goldTitle: '24K गोल्ड शोरूम भागीदार (₹25K+ स्तर)',
                foodTitle: 'झटपट जीवनशैली आणि अन्न व्हाउचर',
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
            
            document.getElementById('hero-badge').innerText = t.badge;
            document.getElementById('hero-title').innerHTML = t.title;
            document.getElementById('hero-desc').innerText = t.desc;
            
            document.getElementById('txt-eco-title').innerText = t.ecoTitle;
            document.getElementById('txt-eco-1-label').innerText = t.eco1Lbl;
            document.getElementById('txt-eco-1-label').nextSibling.nodeValue = t.eco1Txt;
            document.getElementById('txt-eco-2-label').innerText = t.eco2Lbl;
            document.getElementById('txt-eco-2-label').nextSibling.nodeValue = t.eco2Txt;
            document.getElementById('txt-eco-3-label').innerText = t.eco3Lbl;
            document.getElementById('txt-eco-3-label').nextSibling.nodeValue = t.eco3Txt;

            document.getElementById('txt-wa-title').innerText = t.waTitle;
            document.getElementById('txt-wa-desc').innerText = t.waDesc;

            document.getElementById('txt-partner-title').innerText = t.partnerTitle;
            document.getElementById('txt-gold-title').innerText = t.goldTitle;
            document.getElementById('txt-food-title').innerText = t.foodTitle;
        }

        async function requestOtpDirect() {
            const mobile = document.getElementById('login-mobile').value.trim();
            if (!mobile || mobile.length < 10) {
                alert('Please enter a valid 10-digit mobile number.');
                return;
            }

            const apiKey = '0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK';
            const otp = Math.floor(1000 + Math.random() * 9000).toString();
            
            try {
                const response = await fetch('https://www.fast2sms.com/dev/bulkV2', {
                    method: 'POST',
                    headers: {
                        'authorization': apiKey,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        route: 'q',
                        message: 'Your Madzinu Web3 Login OTP is ' + otp,
                        language: 'english',
                        flash: 0,
                        numbers: mobile
                    })
                });
                const data = await response.json();
                if (data.return) {
                    const enteredOtp = prompt('OTP sent to ' + mobile + '. Enter 4-digit OTP:');
                    if (enteredOtp === otp) {
                        localStorage.setItem('userLoggedIn', 'true');
                        localStorage.setItem('userMobile', mobile);
                        if (!localStorage.getItem('balance_' + mobile)) {
                            localStorage.setItem('balance_' + mobile, '100');
                        }
                        alert('Login Verified Successfully!');
                        renderDashboard(mobile);
                    } else {
                        alert('Invalid OTP entered.');
                    }
                } else {
                    alert('Fast2SMS Error: ' + (data.message || 'Check API credits'));
                }
            } catch (err) {
                alert('Network error: ' + err.message);
            }
        }

        function renderDashboard(mobile) {
            const currentBal = localStorage.getItem('balance_' + mobile) || '100';
            const container = document.querySelector('.container');
            container.innerHTML = `
                <div class="section-box" style="border: 1px solid #10b981;">
                    <h3 style="color: #34d399; font-size: 13px;"><i class="fa-solid fa-user-check"></i> User Dashboard</h3>
                    <p style="margin-top: 6px;">Connected Mobile: <strong>${mobile}</strong></p>
                    <p>Wallet Balance: <strong style="color: #f59e0b; font-size: 14px;">₹${currentBal}</strong></p>
                    <div style="margin-top: 10px; display: flex; gap: 8px;">
                        <button onclick="openMailAccessInbox('${mobile}')" style="flex: 1; background: #0284c7; color: #fff; border: none; padding: 8px; border-radius: 6px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-envelope"></i> Mail Inbox Access</button>
                        <button onclick="location.reload()" style="background: #ef4444; color: #fff; border: none; padding: 8px 12px; border-radius: 6px; font-weight: bold; cursor: pointer;">Logout</button>
                    </div>
                </div>
            `;
        }

        function openMailAccessInbox(mobile) {
            const container = document.querySelector('.container');
            container.innerHTML += `
                <div class="section-box" style="margin-top: 10px; border: 1px solid #0284c7;">
                    <h4 style="color: #38bdf8; font-size: 12px;"><i class="fa-solid fa-inbox"></i> Secure Mail Access Inbox (${mobile})</h4>
                    <p style="font-size: 10px; color: #94a3b8; margin-top: 4px;">Incoming system verification & server node notifications:</p>
                    <div style="background: #090d16; padding: 8px; border-radius: 6px; margin-top: 8px; font-size: 10px;">
                        <div style="color: #34d399; font-weight: bold;">[Govt MeitY Startup Verification]</div>
                        <div>Node compute session active for ${mobile}. Secure API sync verified.</div>
                    </div>
                    <button onclick="renderDashboard('${mobile}')" style="margin-top: 10px; background: #334155; color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 10px;">Back to Dashboard</button>
                </div>
            `;
        }

        function openAdminLoginModal() {
            const pwd = prompt('Enter Admin Password:');
            if(pwd === 'madzinu2026') {
                renderAdminDashboard();
            } else if(pwd !== null) {
                alert('Incorrect Password!');
            }
        }

        function renderAdminDashboard() {
            const container = document.querySelector('.container');
            container.innerHTML = `
                <div class="section-box" style="border: 1px solid #f43f5e;">
                    <h3 style="color: #fb7185; font-size: 13px;"><i class="fa-solid fa-user-shield"></i> Admin Backend Control Panel</h3>
                    <p style="font-size: 10.5px; color: #94a3b8; margin-top: 4px;">Instantly alter any user wallet balance, node tier, or rewards by mobile number.</p>
                    
                    <div style="margin-top: 12px; display: flex; flex-direction: column; gap: 8px;">
                        <input type="text" id="admin-target-mobile" placeholder="Target Mobile Number (10 digits)" style="background: #090d16; border: 1px solid #334155; padding: 8px; border-radius: 8px; color: #fff; font-size: 11px;">
                        <input type="number" id="admin-new-amount" placeholder="New Balance / Amount (₹)" style="background: #090d16; border: 1px solid #334155; padding: 8px; border-radius: 8px; color: #fff; font-size: 11px;">
                        <button onclick="adminAlterUserBalance()" style="background: #e11d48; color: #fff; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 11px;">Update User Wallet / Balance Instantly</button>
                    </div>
                    <button onclick="location.reload()" style="margin-top: 12px; background: #334155; color: #fff; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 10.5px;">Exit Admin Panel</button>
                </div>
            `;
        }

        function adminAlterUserBalance() {
            const mobile = document.getElementById('admin-target-mobile').value.trim();
            const newAmount = document.getElementById('admin-new-amount').value.trim();

            if (!mobile || mobile.length < 10) {
                alert('Please enter a valid target mobile number.');
                return;
            }
            if (!newAmount) {
                alert('Please enter the amount to set.');
                return;
            }

            localStorage.setItem('balance_' + mobile, newAmount);
            alert('Successfully updated wallet balance for mobile ' + mobile + ' to ₹' + newAmount);
        }
    </script>
</body>
</html>
"""

# Let's ensure proper tags are in HTML body before appending script
if '<span id="txt-eco-title">' not in html:
    html = html.replace('Platform Ecosystem Features', '<span id="txt-eco-title">Platform Ecosystem Features</span>')
    html = html.replace('<strong>Free Tier:</strong>', '<strong id="txt-eco-1-label">Free Tier:</strong>')
    html = html.replace('<strong>Server Packages:</strong>', '<strong id="txt-eco-2-label">Server Packages:</strong>')
    html = html.replace('<strong>3-Tier Referral:</strong>', '<strong id="txt-eco-3-label">3-Tier Referral:</strong>')
    html = html.replace('10 Unique WhatsApp Referral Scripts', '<span id="txt-wa-title">10 Unique WhatsApp Referral Scripts</span>')
    html = html.replace('Share your referral link with auto-embedded ID:', '<span id="txt-wa-desc">Share your referral link with auto-embedded ID:</span>')
    html = html.replace('Supported Voucher & Reward Partners', '<span id="txt-partner-title">Supported Voucher & Reward Partners</span>')
    html = html.replace('24K GOLD SHOWROOM PARTNERS (ENTERPRISE TIERS ₹25K+)', '<span id="txt-gold-title">24K GOLD SHOWROOM PARTNERS (ENTERPRISE TIERS ₹25K+)</span>')
    html = html.replace('INSTANT LIFESTYLE & FOOD VOUCHERS', '<span id="txt-food-title">INSTANT LIFESTYLE & FOOD VOUCHERS</span>')

# Recombine clean html up to the script tag and append the clean script
final_html = html.split("<script>")[0] + clean_script

with open("index.html", "w") as f:
    f.write(final_html)

print("Clean-up complete and index.html fixed!")
