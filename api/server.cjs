const express = require('express');
const https = require('https');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static assets if needed
app.use(express.static('public'));

app.post('/api/send-otp', (req, res) => {
  const { phone, otp } = req.body;
  const apiKey = '0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK';
  const message = `Your Madzinu Web3 verification OTP is ${otp}`;
  const encodedMsg = encodeURIComponent(message);
  
  const url = `https://www.fast2sms.com/dev/bulkV2?authorization=${apiKey}&route=q&sender_id=TXTIND&message=${encodedMsg}&flash=0&numbers=${phone}`;

  https.get(url, (apiRes) => {
    let data = '';
    apiRes.on('data', (chunk) => { data += chunk; });
    apiRes.on('end', () => {
      try {
        const parsed = JSON.parse(data);
        res.json({ success: true, response: parsed });
      } catch (e) {
        res.json({ success: true, raw: data });
      }
    });
  }).on('error', (err) => {
    res.status(500).json({ success: false, error: err.message });
  });
});

module.exports = app;
