const https = require('https');

export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ success: false, message: 'Method not allowed' });
    }

    const { phone } = req.body;
    if (!phone) {
        return res.status(400).json({ success: false, message: 'Phone number is required' });
    }

    // Generate a 6-digit OTP
    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    const apiKey = "0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK";

    const data = JSON.stringify({
        route: "q",
        message: `Your Madzinu Web3 Portal OTP is ${otp}`,
        language: "english",
        flash: 0,
        numbers: phone
    });

    const options = {
        hostname: 'www.fast2sms.com',
        path: '/dev/bulkV2',
        method: 'POST',
        headers: {
            'authorization': apiKey,
            'Content-Type': 'application/json',
            'Content-Length': data.length
        }
    };

    return new Promise((resolve) => {
        const fastReq = https.request(options, (fastRes) => {
            let body = '';
            fastRes.on('data', (chunk) => { body += chunk; });
            fastRes.on('end', () => {
                try {
                    const result = JSON.parse(body);
                    if (result.return) {
                        // Store OTP in memory/response for verification (or handle via session)
                        resolve(res.status(200).json({ success: true, otp: otp, message: 'OTP sent successfully' }));
                    } else {
                        resolve(res.status(400).json({ success: false, message: result.message || 'Failed to send SMS' }));
                    }
                } catch (e) {
                    resolve(res.status(500).json({ success: false, message: 'Parsing error from gateway' }));
                }
            });
        });

        fastReq.on('error', (error) => {
            resolve(res.status(500).json({ success: false, message: error.message }));
        });

        fastReq.write(data);
        fastReq.end();
    });
}
