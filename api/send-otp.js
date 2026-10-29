const https = require('https');

module.exports = async (req, res) => {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    const { number } = req.body;
    if (!number) {
        return res.status(400).json({ error: 'Mobile number required' });
    }

    const apiKey = process.env.FAST2SMS_API_KEY;
    if (!apiKey) {
        return res.status(500).json({ error: 'Fast2SMS API Key not configured in environment variables' });
    }

    const otp = Math.floor(1000 + Math.random() * 9000).toString();
    
    // Fast2SMS official payload structure for OTP route
    const postData = JSON.stringify({
        route: 'otp',
        variables_values: otp,
        numbers: number
    });

    const options = {
        hostname: 'www.fast2sms.com',
        port: 443,
        path: '/dev/bulkV2',
        method: 'POST',
        headers: {
            'authorization': apiKey,
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };

    const fastReq = https.request(options, (fastRes) => {
        let data = '';
        fastRes.on('data', (chunk) => { data += chunk; });
        fastRes.on('end', () => {
            try {
                const jsonResponse = JSON.parse(data || '{}');
                res.status(200).json({ success: true, message: 'OTP dispatched via Fast2SMS', response: jsonResponse, debug_otp: otp });
            } catch (e) {
                res.status(200).json({ success: true, raw: data });
            }
        });
    });

    fastReq.on('error', (error) => {
        res.status(500).json({ success: false, error: error.message });
    });

    fastReq.write(postData);
    fastReq.end();
};
