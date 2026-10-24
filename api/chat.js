export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const userMessage = req.body.prompt || req.body.message || "Hello";
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    return res.status(200).json({ reply: "CRITICAL ERROR: GEMINI_API_KEY is not set in Vercel environment variables." });
  }

  const systemPrompt = `You are the official, expert AI Customer Support Assistant for Madzinu Web3 Technologies (madzinuweb3technologies.in), registered and operating out of Chennai, Tamil Nadu. 
  
  Complete Business & Operational Context:
  - Enterprises: Madzinu Web3 Technologies and Cosmogems, operating in Chennai, Tamil Nadu.
  - Core Focus & Services: Web3 development, blockchain solutions, custom web and terminal applications, digital automation, and secure decentralized integrations.
  - E-commerce & Product Lines: High-quality solar-dried vegetable and botanical powders, eco-friendly distribution, and private-label skincare lines under the brand MADZINU.
  - Support Email: support@madzinuweb3technologies.com

  Answer all client questions accurately and professionally based on this full context. Maintain an expert, helpful, and welcoming tone.`;

  try {
    const apiResponse = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ role: "user", parts: [{ text: `${systemPrompt}\n\nClient Question: ${userMessage}` }] }]
      })
    });

    const data = await apiResponse.json();
    
    if (data.error) {
      return res.status(200).json({ reply: `Gemini API Error: ${data.error.message}` });
    }

    const replyText = data.candidates?.[0]?.content?.parts?.[0]?.text;
    if (!replyText) {
      return res.status(200).json({ reply: "CRITICAL ERROR: Empty response received from Gemini API model." });
    }

    return res.status(200).json({ reply: replyText });
  } catch (err) {
    return res.status(200).json({ reply: `Server Exception: ${err.message}` });
  }
}
