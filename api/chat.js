export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const userMessage = req.body.prompt || req.body.message || "Hello";
  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    return res.status(200).json({ reply: "CRITICAL ERROR: GEMINI_API_KEY is not set." });
  }

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 6000);

  try {
    const apiResponse = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ role: "user", parts: [{ text: `You are the AI assistant for Madzinu Web3 Technologies, owned by Sampath Madhan in Chennai. Answer: ${userMessage}` }] }]
      }),
      signal: controller.signal
    });

    clearTimeout(timeoutId);
    const data = await apiResponse.json();
    
    if (data.error) {
      return res.status(200).json({ reply: `API Error: ${data.error.message}` });
    }

    const replyText = data.candidates?.[0]?.content?.parts?.[0]?.text;
    return res.status(200).json({ reply: replyText || "Welcome to Madzinu Web3 Technologies. How can we assist you?" });
  } catch (err) {
    clearTimeout(timeoutId);
    return res.status(200).json({ reply: "Welcome to Madzinu Web3 Technologies, owned by Sampath Madhan in Chennai. How can we help you today?" });
  }
}
