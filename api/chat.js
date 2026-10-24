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

  const systemPrompt = `You are the official AI Customer Support Assistant for Madzinu Web3 Technologies and Cosmogems, owned and operated by Sampath Madhan in Chennai, Tamil Nadu. 
  
  Core Services & Products:
  - Web3 development, blockchain solutions, custom web/terminal applications, and digital automation.
  - Eco-friendly solar-dried vegetable/botanical powders and MADZINU private-label skincare.
  - Support: support@madzinuweb3technologies.com

  Keep answers professional, direct, and accurate.`;

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
      return res.status(200).json({ reply: "Service is temporarily busy. Please try again." });
    }

    return res.status(200).json({ reply: replyText });
  } catch (err) {
    return res.status(200).json({ reply: `Server Exception: ${err.message}` });
  }
}
