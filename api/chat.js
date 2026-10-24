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

  // Comprehensive company knowledge base for Gemini
  const systemPrompt = `You are the official, highly knowledgeable AI Customer Support Assistant for Madzinu Web3 Technologies (madzinuweb3technologies.in), registered and operating out of Chennai, Tamil Nadu. 
  
  Key business details:
  - Enterprise: Madzinu Web3 Technologies & Cosmogems.
  - Core Focus: Web3 development, blockchain solutions, custom web applications, digital automation, and specialized product offerings.
  - Support Email: support@madzinuweb3technologies.com
  
  Your job is to answer user queries accurately based on this context, assist them with their inquiries about the site, products, or services, and maintain a professional, helpful, and welcoming tone. If you are unsure about specific custom client billing data, invite them to reach out directly to support@madzinuweb3technologies.com.`;

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
