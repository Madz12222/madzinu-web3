import fs from 'fs';

const htmlPath = 'public/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

const newScripts = [
    "🚀 Want to earn ₹100 Daily with just 500 simple micro-tasks? Madzinu Web3 Technologies is India's 1st Autonomous AI Studio & Cloud Network (Govt. of India Recognized Startup under MeitY)[span_0](start_span)[span_0](end_span). ✅ Free Tier Available: Complete daily tasks & withdraw instantly[span_1](start_span)[span_1](end_span). 💻 Enterprise Cloud Packages: Ranging from ₹2,000 to ₹1,00,000 with high-throughput server remuneration over 14 days[span_2](start_span)[span_2](end_span). 👉 Launch your secure node now: https://madzinuweb3technologies.in",
    
    "⚡ Want to Scale Your Compute Power with Sovereign Cloud Nodes? Join India's leading decentralized cloud network at Madzinu Web3 Technologies[span_3](start_span)[span_3](end_span). 🖥️ High-performance vCPU & NVMe storage server allocations. 💼 Professional 14-day task remuneration cycles[span_4](start_span)[span_4](end_span). 🇮🇳 Recognized Startup under MeitY (Govt. of India)[span_5](start_span)[span_5](end_span). 👉 Explore server tiers & activate your node: https://madzinuweb3technologies.in",
    
    "📦 Amazon, Flipkart & Meesho Fulfillment Node Sync! Turn your mobile device into an automated digital jobwork hub with Madzinu Web3 Technologies[span_6](start_span)[span_6](end_span): 🔍 SKU audit logs & logistics routing checks[span_7](start_span)[span_7](end_span). 💰 Daily micro-task payouts with a minimum withdrawal of just ₹100[span_8](start_span)[span_8](end_span). 🚀 MeitY Recognized & fully automated[span_9](start_span)[span_9](end_span). 👉 Start your daily tasks today: https://madzinuweb3technologies.in",
    
    "💎 Earn 10% - 12% Dynamic Referral Bonuses + Exclusive 24K Gold Vault Access! Build your network with Madzinu Web3 Technologies[span_10](start_span)[span_10](end_span): 📈 Unlock exclusive gold vault conversion benefits on enterprise server tiers (₹25,000+)[span_11](start_span)[span_11](end_span). ⚡ Instant automated email & SMS confirmations on all activations. 👉 Join the network & share your link: https://madzinuweb3technologies.in",
    
    "⏰ High-Throughput Server Slots Opening Now! Secure your infrastructure package with Madzinu Web3 Technologies before capacity fills up[span_12](start_span)[span_12](end_span): 💼 Server packages from ₹2,000 to ₹1,00,000[span_13](start_span)[span_13](end_span). 🚀 14-day professional remuneration cycle[span_14](start_span)[span_14](end_span). 🛡️ Govt. of India Recognized Startup (MeitY)[span_15](start_span)[span_15](end_span). 👉 Secure your node instantly: https://madzinuweb3technologies.in",
    
    "📱 Spend 10 minutes a day? Turn your free time into daily cash! 💼 Free Tier: Complete 500 daily micro-tasks (₹0.20/task) to earn ₹100 daily[span_16](start_span)[span_16](end_span). ⚡ Instant payouts & zero delay. 🇮🇳 Powered by Madzinu Web3 Technologies (MeitY Recognized)[span_17](start_span)[span_17](end_span). 👉 Register and start earning now: https://madzinuweb3technologies.in",
    
    "🔒 Institutional-Grade Cloud Compute & Automated Jobworks backed by robust MongoDB architecture, Hostinger SMTP receipts, and instant SMS verification: 🏢 Govt. of India Recognized Startup[span_18](start_span)[span_18](end_span). 📊 Transparent e-commerce catalog pricing & vendor order feeds[span_19](start_span)[span_19](end_span). 👉 Explore the ecosystem: https://madzinuweb3technologies.in",
    
    "🌟 Unlock 24K Gold Vault Conversion with Enterprise Tiers! Take your earnings to the next level with Madzinu Web3 Technologies[span_20](start_span)[span_20](end_span): 💰 10% - 12% Dynamic Referral Bonuses[span_21](start_span)[span_21](end_span). 🚀 Premium server packages with high-throughput 14-day returns[span_22](start_span)[span_22](end_span). 👉 Upgrade your tier today: https://madzinuweb3technologies.in",
    
    "🔥 India's 1st Autonomous AI Studio & Cloud Network is LIVE[span_23](start_span)[span_23](end_span)! Earn ₹100 daily via micro-tasks or deploy enterprise server nodes (₹2,000 to ₹1,00,000) with 14-day professional remuneration[span_24](start_span)[span_24](end_span). Govt. of India Recognized (MeitY)[span_25](start_span)[span_25](end_span). 👉 Check it out here: https://madzinuweb3technologies.in",
    
    "🚀 Building the Future of Decentralized Cloud Compute in India. Madzinu Web3 Technologies combines automated e-commerce jobworks, secure cloud nodes, and high-yield enterprise packages under a MeitY-recognized startup framework[span_26](start_span)[span_26](end_span). 👉 Join our growing network: https://madzinuweb3technologies.in"
];

// Loop through and update onclick or text handlers for script 1 to 10
for (let i = 0; i < newScripts.length; i++) {
    const scriptNum = i + 1;
    // Replace share function or text content pattern safely
    const encodedMsg = encodeURIComponent(newScripts[i]);
    
    // We look for shareWhatsApp(scriptNum) or similar patterns in onclick
    const regex = new RegExp(`onclick=["'][^"']*shareWhatsApp\\(\\s*${scriptNum}\\s*\\)[^"']*["']`, 'gi');
    // Alternatively, replace the text inside function handler array if present
    html = html.replace(new RegExp(`['"]${scriptNum}['"]\\s*:\\s*['"][^'"]*['"]`, 'g'), `'${scriptNum}': '${newScripts[i].replace(/'/g, "\\'")}'`);
}

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('✅ WhatsApp script buttons updated successfully in public/index.html!');
