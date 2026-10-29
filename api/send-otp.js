const https = require('https');

module.exports = async (req, res) => {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    const { number } = req.body;
    if (!number) {
        return res.status(400).json({ error: 'Mobile number required' });
    }

    // Fast2SMS API integration parameters
    const apiKey = process.env.FAST2SMS_API_KEY || 'YOUR_FAST2SMS_API_KEY';
    const otp = Math.floor(100000 + Math.random() * 900000);
    
    const postData = JSON.stringify({
        route: 'v3',
        sender_id: 'TXTIND',
        message: `Your verification OTP for Madzinu Web3 Technologies is ${otp}`,
        language: 'english',
        flash: 0,
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
            'Content-Length': postData.length
        }
    };

    const fastReq = https.request(options, (fastRes) => {
        let data = '';
        fastRes.on('data', (chunk) => { data += chunk; });
        fastRes.on('end', () => {
            res.status(200).json({ success: true, message: 'OTP dispatched via Fast2SMS', response: JSON.parse(data || '{}') });
        });
    });

    fastReq.on('error', (error) => {
        res.status(500).json({ success: false, error: error.message });
    });

    fastReq.write(postData);
    fastReq.end();
};
