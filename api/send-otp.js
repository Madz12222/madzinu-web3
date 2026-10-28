const https = require('https');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (e) { body = {}; }
    }
    if (!body) body = {};

    const phone = body.phone || req.query.phone;
    const otp = body.otp || req.query.otp || Math.floor(100000 + Math.random() * 900000).toString();

    if (!phone) {
      return res.status(400).json({ success: false, message: 'Phone number required' });
    }

    const apiKey = '0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK';
    const message = `Your Madzinu Web3 verification OTP is ${otp}`;
    const encodedMsg = encodeURIComponent(message);
    
    const url = `https://www.fast2sms.com/dev/bulkV2?authorization=${apiKey}&route=q&message=${encodedMsg}&flash=0&numbers=${phone}`;

    https.get(url, (apiRes) => {
      let responseData = '';
      apiRes.on('data', chunk => { responseData += chunk; });
      apiRes.on('end', () => {
        let parsedFast2SMS = {};
        try {
          parsedFast2SMS = JSON.parse(responseData);
        } catch (e) {
          parsedFast2SMS = { raw: responseData };
        }
        return res.status(200).json({
          success: true,
          otp: otp,
          fast2sms: parsedFast2SMS
        });
      });
    }).on('error', (err) => {
      return res.status(500).json({ success: false, error: err.message });
    });

  } catch (err) {
    return res.status(500).json({ success: false, error: err.message });
  }
};
