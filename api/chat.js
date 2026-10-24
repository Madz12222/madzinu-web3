export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const userMessage = (req.body.prompt || req.body.message || "").toLowerCase();

  let replyText = "Welcome to **Madzinu Web3 Technologies**! We are a Govt. of India Recognized Startup under MeitY with IndiaAI Portal approved compute access (Reg No: ST20260926506), owned by Sampath Madhan in Chennai. We provide sovereign cloud compute packages, autonomous e-commerce jobworks, and enterprise reward ecosystems. How can we assist you today?";

  if (userMessage.includes("owner") || userMessage.includes("who")) {
    replyText = "**Madzinu Web3 Technologies** and **Cosmogems** are owned and operated by **Sampath Madhan** from Chennai, Tamil Nadu.";
  } else if (userMessage.includes("offer") || userMessage.includes("what is") || userMessage.includes("site") || userMessage.includes("about")) {
    replyText = "Madzinu Web3 Technologies is India's first autonomous AI studio & cloud network, recognized by the Govt. of India (MeitY) and approved by the IndiaAI Portal (Reg No: ST20260926506). We offer:\n* **Cloud Compute Licenses**: High-throughput server compute packages from ₹2,000 to ₹1,00,000 with 14-day validity.\n* **Autonomous Jobworks**: Daily automated verification micro-tasks for Amazon, Flipkart, and Meesho.\n* **Reward Ecosystems**: Dynamic referral bonuses and 24K gold showroom voucher redemptions for enterprise tiers (₹25k+).";
  } else if (userMessage.includes("server") || userMessage.includes("compute") || userMessage.includes("package") || userMessage.includes("tier") || userMessage.includes("price")) {
    replyText = "We offer 14-day SaaS Cloud Computing & E-Commerce Jobwork licenses ranging from ₹2,000 to ₹1,00,000 (+ 18% GST). These packages allow contractors to execute daily automated task workloads for platforms like Amazon, Flipkart, and Meesho with professional remuneration.";
  } else if (userMessage.includes("task") || userMessage.includes("jobwork") || userMessage.includes("amazon") || userMessage.includes("flipkart") || userMessage.includes("meesho") || userMessage.includes("earn")) {
    replyText = "Our platform features daily e-commerce jobworks:\n* **Free Tier**: Complete 500 daily micro-tasks (₹0.20/task) to earn ₹100 daily with a ₹100 minimum withdrawal threshold.\n* **Node Workloads**: Automated fulfillment center node sync, SKU audit logs, logistics routing, and catalog pricing verification.";
  } else if (userMessage.includes("gold") || userMessage.includes("voucher") || userMessage.includes("reward") || userMessage.includes("tanishq") || userMessage.includes("swiggy")) {
    replyText = "Enterprise server tiers (₹25,000+) unlock exclusive 24K gold vault showroom voucher redemptions with partners like Tanishq, Malabar Gold, GRT Jewellers, and Kalyan Jewellers, alongside instant lifestyle & food vouchers for Swiggy, Zomato, Blinkit, and Amazon Pay.";
  } else if (userMessage.includes("contact") || userMessage.includes("support") || userMessage.includes("email")) {
    replyText = "For assistance and enterprise inquiries, please reach out directly at **support@madzinuweb3technologies.com**.";
  }

  return res.status(200).json({ reply: replyText });
}
