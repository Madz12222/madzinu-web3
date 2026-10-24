export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const userMessage = (req.body.prompt || req.body.message || "").toLowerCase();

  let replyText = "Welcome to **Madzinu Web3 Technologies**! Based in Chennai, Tamil Nadu, we specialize in delivering cutting-edge digital infrastructure, Web3 & blockchain solutions, custom web and terminal applications, and digital automation. In addition, our broader enterprise operations with **Cosmogems** support eco-friendly commercial initiatives, solar-dried botanical powders, and MADZINU private-label skincare. How can we assist you today? Reach us at support@madzinuweb3technologies.com.";

  if (userMessage.includes("owner") || userMessage.includes("who")) {
    replyText = "**Madzinu Web3 Technologies** and **Cosmogems** are owned and operated by **Sampath Madhan** from Chennai, Tamil Nadu.";
  } else if (userMessage.includes("service") || userMessage.includes("blockchain") || userMessage.includes("smart contract")) {
    replyText = "Our core technology services include:\n* **Web3 & Blockchain Solutions**: Custom dApp development, smart contract architecture, deployment, and auditing.\n* **Custom Web & Terminal Applications**: Full-stack web design and specialized CLI tools.\n* **Digital Automation**: Intelligent process automation to streamline business workflows.";
  } else if (userMessage.includes("product") || userMessage.includes("skincare") || userMessage.includes("powder") || userMessage.includes("cosmogems")) {
    replyText = "Through our **Cosmogems** and **MADZINU** initiatives, we offer high-quality solar-dried vegetable/botanical powders and private-label skincare lines.";
  } else if (userMessage.includes("contact") || userMessage.includes("support") || userMessage.includes("email")) {
    replyText = "You can directly reach our team at **support@madzinuweb3technologies.com** for any project inquiries or business consultations.";
  }

  return res.status(200).json({ reply: replyText });
}
