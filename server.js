const express = require('express');
const https = require('https');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/api/send-otp', (req, res) => {
    const { phone } = req.body;
    if (!phone) {
        return res.status(400).json({ success: false, message: 'Phone number is required' });
    }

    const otp = Math.floor(100000 + Math.random() * 900000);
    const apiKey = "0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK";
    const message = `Madzinu Web3: Your secure login OTP is ${otp}`;
    const encodedMsg = encodeURIComponent(message);
    
    const smsUrl = `https://www.fast2sms.com/dev/bulkV2?authorization=${apiKey}&route=q&message=${encodedMsg}&language=english&flash=0&numbers=${phone}`;

    https.get(smsUrl, (smsRes) => {
        let data = '';
        smsRes.on('data', (chunk) => { data += chunk; });
        smsRes.on('end', () => {
            console.log("Fast2SMS Response:", data);
            try {
                const parsed = JSON.parse(data);
                if (parsed.return) {
                    res.json({ success: true, message: 'OTP sent successfully', otp });
                } else {
                    res.json({ success: false, message: 'Failed to send SMS via Fast2SMS', details: parsed });
                }
            } catch (e) {
                res.json({ success: true, message: 'OTP triggered successfully', otp });
            }
        });
    }).on('error', (err) => {
        console.error("SMS Error:", err);
        res.status(500).json({ success: false, message: err.message });
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
