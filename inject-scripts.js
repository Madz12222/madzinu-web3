import fs from 'fs';

const htmlPath = 'public/index.html';
if (!fs.existsSync(htmlPath)) {
    console.error('❌ public/index.html not found!');
    process.exit(1);
}

let html = fs.readFileSync(htmlPath, 'utf8');

const newScripts = [
    "🚀 Want to earn ₹100 Daily with just 500 simple micro-tasks? Madzinu Web3 Technologies is India's 1st Autonomous AI Studio & Cloud Network (Govt. of India Recognized Startup under MeitY). ✅ Free Tier Available: Complete daily tasks & withdraw instantly. 💻 Enterprise Cloud Packages: Ranging from ₹2,000 to ₹1,00,000 with high-throughput server remuneration over 14 days. 👉 Launch your secure node now: https://madzinuweb3technologies.in",
    
    "⚡ Want to Scale Your Compute Power with Sovereign Cloud Nodes? Join India's leading decentralized cloud network at Madzinu Web3 Technologies. 🖥️ High-performance vCPU & NVMe storage server allocations. 💼 Professional 14-day task remuneration cycles. 🇮🇳 Recognized Startup under MeitY (Govt. of India). 👉 Explore server tiers & activate your node: https://madzinuweb3technologies.in",
    
    "📦 Amazon, Flipkart & Meesho Fulfillment Node Sync! Turn your mobile device into an automated digital jobwork hub with Madzinu Web3 Technologies: 🔍 SKU audit logs & logistics routing checks. 💰 Daily micro-task payouts with a minimum withdrawal of just ₹100. 🚀 MeitY Recognized & fully automated. 👉 Start your daily tasks today: https://madzinuweb3technologies.in",
    
    "💎 Earn 10% - 12% Dynamic Referral Bonuses + Exclusive 24K Gold Vault Access! Build your network with Madzinu Web3 Technologies: 📈 Unlock exclusive gold vault conversion benefits on enterprise server tiers (₹25,000+). ⚡ Instant automated email & SMS confirmations on all activations. 👉 Join the network & share your link: https://madzinuweb3technologies.in",
    
    "⏰ High-Throughput Server Slots Opening Now! Secure your infrastructure package with Madzinu Web3 Technologies before capacity fills up: 💼 Server packages from ₹2,000 to ₹1,00,000. 🚀 14-day professional remuneration cycle. 🛡️ Govt. of India Recognized Startup (MeitY). 👉 Secure your node instantly: https://madzinuweb3technologies.in",
    
    "📱 Spend 10 minutes a day? Turn your free time into daily cash! 💼 Free Tier: Complete 500 daily micro-tasks (₹0.20/task) to earn ₹100 daily. ⚡ Instant payouts & zero delay. 🇮🇳 Powered by Madzinu Web3 Technologies (MeitY Recognized). 👉 Register and start earning now: https://madzinuweb3technologies.in",
    
    "🔒 Institutional-Grade Cloud Compute & Automated Jobworks backed by robust MongoDB architecture, Hostinger SMTP receipts, and instant SMS verification: 🏢 Govt. of India Recognized Startup. 📊 Transparent e-commerce catalog pricing & vendor order feeds. 👉 Explore the ecosystem: https://madzinuweb3technologies.in",
    
    "🌟 Unlock 24K Gold Vault Conversion with Enterprise Tiers! Take your earnings to the next level with Madzinu Web3 Technologies: 💰 10% - 12% Dynamic Referral Bonuses. 🚀 Premium server packages with high-throughput 14-day returns. 👉 Upgrade your tier today: https://madzinuweb3technologies.in",
    
    "🔥 India's 1st Autonomous AI Studio & Cloud Network is LIVE! Earn ₹100 daily via micro-tasks or deploy enterprise server nodes (₹2,000 to ₹1,00,000) with 14-day professional remuneration. Govt. of India Recognized (MeitY). 👉 Check it out here: https://madzinuweb3technologies.in",
    
    "🚀 Building the Future of Decentralized Cloud Compute in India. Madzinu Web3 Technologies combines automated e-commerce jobworks, secure cloud nodes, and high-yield enterprise packages under a MeitY-recognized startup framework. 👉 Join our growing network: https://madzinuweb3technologies.in"
];

// Replace old whatsapp scripts array or variable in html
// We search for the javascript array assignment and update it
const scriptRegex = /const\s+whatsappScripts\s*=\s*\[[\s\S]*?\];/;
if (scriptRegex.test(html)) {
    html = html.replace(scriptRegex, `const whatsappScripts = ${JSON.stringify(newScripts, null, 4)};`);
    fs.writeFileSync(htmlPath, html, 'utf8');
    console.log('✅ Successfully updated whatsappScripts in public/index.html');
} else {
    console.log('⚠️ whatsappScripts variable not found by regex, checking generic array...');
}
