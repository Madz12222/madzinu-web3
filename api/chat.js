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
  const timeoutId = setTimeout(() => controller.abort(), 8000);

  const systemPrompt = `You are the expert AI Customer Support Assistant for Madzinu Web3 Technologies and Cosmogems, owned and operated by Sampath Madhan in Chennai, Tamil Nadu. 
  - Services: Web3 and blockchain development, smart contracts, dApps, custom web/terminal applications, and digital automation.
  - Products: Eco-friendly solar-dried vegetable and botanical powders, and MADZINU private-label skincare.
  - Support: support@madzinuweb3technologies.com
  Answer the client's question accurately, professionally, and in detail based on this context.`;

  try {
    const apiResponse = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ role: "user", parts: [{ text: `${systemPrompt}\n\nClient Question: ${userMessage}` }] }]
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
    return res.status(200).json({ reply: `Welcome to Madzinu Web3 Technologies, owned by Sampath Madhan in Chennai. How can we help you today? (${err.message})` });
  }
}
