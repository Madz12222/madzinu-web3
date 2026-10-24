export default async function handler(req, res) {
  // Set CORS headers so your WordPress site can call this Vercel function smoothly
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
  const systemPrompt = req.body.system || "You are the official Customer Support AI for Madzinu Web3 Technologies.";
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    return res.status(200).json({ reply: "API key is not configured in Vercel environment variables." });
  }

  try {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [
          { role: "user", parts: [{ text: `${systemPrompt}\n\nUser Question: ${userMessage}` }] }
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
