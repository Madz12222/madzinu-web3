import fs from 'fs';

const htmlPath = 'public/index.html';
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

// Replace the javascript function or array holding the messages
// If there is an array called whatsappScripts or similar, update it, otherwise inject the global array
if (html.includes('whatsappScripts')) {
    html = html.replace(/const\s+whatsappScripts\s*=\s*\[[\s\S]*?\];/, `const whatsappScripts = ${JSON.stringify(newScripts, null, 4)};`);
} else {
    // Inject the array right before closing body or in script tag
    const scriptInjection = `\n<script>\nconst whatsappScripts = ${JSON.stringify(newScripts, null, 4)};\nfunction shareWhatsApp(index) {\n  const msg = encodeURIComponent(whatsappScripts[index - 1]);\n  window.open('https://api.whatsapp.com/send?text=' + msg, '_blank');\n}\n</script>\n`;
    html = html.replace('</body>', scriptInjection + '</body>');
}

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('✅ WhatsApp scripts successfully injected into HTML!');
