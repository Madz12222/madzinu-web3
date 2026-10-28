const https = require('https');

module.exports = (req, res) => {
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,POST,PUT');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  let body = '';
  req.on('data', chunk => { body += chunk; });
  req.on('end', () => {
    let parsedBody = {};
    try { if (body) parsedBody = JSON.parse(body); } catch (e) {}

    const phone = parsedBody.phone || req.query.phone;
    const otp = parsedBody.otp || req.query.otp || Math.floor(100000 + Math.random() * 900000);

    if (!phone) {
      return res.status(400).json({ success: false, message: 'Phone number required' });
    }

    const apiKey = '0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK';
    const message = `Your Madzinu Web3 verification OTP is ${otp}`;
    const encodedMsg = encodeURIComponent(message);
    
    const url = `https://www.fast2sms.com/dev/bulkV2?authorization=${apiKey}&route=q&message=${encodedMsg}&flash=0&numbers=${phone}`;

    https.get(url, (apiRes) => {
      let data = '';
      apiRes.on('data', (chunk) => { data += chunk; });
      apiRes.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          res.status(200).json({ success: true, response: parsed });
        } catch (e) {
          res.status(200).json({ success: true, raw: data });
        }
      });
    }).on('error', (err) => {
      res.status(500).json({ success: false, error: err.message });
    });
  });
};
