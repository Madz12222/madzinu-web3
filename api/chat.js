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
  } else if (userMessage.includes("reward") || userMessage.includes("gold") || userMessage.includes("1l") || userMessage.includes("1 lakh") || userMessage.includes("tier")) {
    replyText = "For enterprise server tiers (₹25,000+ up to your ₹1,00,000 package), you unlock exclusive **24K Gold Vault Showroom Voucher Redemptions** with premier partners like Tanishq, Malabar Gold, GRT Jewellers, and Kalyan Jewellers, alongside 10%-12% referral bonuses and daily task remuneration!";
  } else if (userMessage.includes("profit") || userMessage.includes("earn") || userMessage.includes("return") || userMessage.includes("remuneration")) {
    replyText = "Our platform provides professional task remuneration over a 14-day cycle. You complete daily automated e-commerce micro-tasks and workspace operations (such as Amazon, Flipkart, and Meesho node syncs) to secure your daily earnings and milestone payouts.";
  } else if (userMessage.includes("server") || userMessage.includes("cost") || userMessage.includes("price") || userMessage.includes("package")) {
    replyText = "We offer 14-day SaaS Cloud Computing & E-Commerce Jobwork licenses ranging from ₹2,000 to ₹1,00,000 (+ 18% GST). Higher tiers unlock maximum task quotas and exclusive 24K gold voucher redemptions.";
  } else if (userMessage.includes("task") || userMessage.includes("jobwork") || userMessage.includes("amazon") || userMessage.includes("flipkart") || userMessage.includes("meesho")) {
    replyText = "Our system runs automated daily e-commerce verification workloads, including fulfillment center node syncs, SKU audit logs, logistics routing, and catalog pricing checks for Amazon, Flipkart, and Meesho.";
  } else if (userMessage.includes("contact") || userMessage.includes("support") || userMessage.includes("email")) {
    replyText = "For immediate support and enterprise project inquiries, reach out directly at **support@madzinuweb3technologies.com**.";
  }

  return res.status(200).json({ reply: replyText });
}
