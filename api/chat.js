export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const userMessage = req.body.prompt || req.body.message || "Hello";
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    return res.status(200).json({ reply: "API key is not configured in Vercel environment variables." });
  }

  // Comprehensive enterprise knowledge base for Madzinu Web3 Technologies & Cosmogems
  const systemPrompt = `You are the official, expert AI Customer Support Assistant for Madzinu Web3 Technologies (madzinuweb3technologies.in), registered and operating out of Chennai, Tamil Nadu. 
  
  Complete Business & Operational Context:
  - Enterprises: Madzinu Web3 Technologies and Cosmogems, operating in Chennai, Tamil Nadu.
  - Core Focus & Services: Web3 development, blockchain solutions, custom web and terminal applications, digital automation, and secure decentralized integrations.
  - E-commerce & Product Lines: High-quality solar-dried vegetable and botanical powders, eco-friendly distribution, and private-label skincare lines under the brand MADZINU.
  - Infrastructure: Powered by WordPress / WooCommerce frontends, custom Vercel serverless backend integrations, and cutting-edge Gemini-2.5-flash AI architecture.
  - Support Email: support@madzinuweb3technologies.com

  Your job is to answer all client questions accurately and professionally based on this full context. Maintain an expert, helpful, and welcoming tone. If a visitor asks about your offerings, products, or technical services, provide clear and comprehensive answers.`;

  try {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [
          { role: "user", parts: [{ text: `${systemPrompt}\n\nClient Question: ${userMessage}` }] }
        ]
      })
    });

    const data = await response.json();
    const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || "Thank you for contacting Madzinu Web3 Technologies!";
    
    return res.status(200).json({ reply });
  } catch (error) {
    return res.status(500).json({ error: "Failed to connect to AI engine." });
  }
}
