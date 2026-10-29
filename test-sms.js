import https from 'https';

const apiKey = process.env.FAST2SMS_API_KEY;
if (!apiKey) {
    console.error('❌ FAST2SMS_API_KEY is not set in environment variables!');
    process.exit(1);
}

const phone = '8122252222';
const otp = Math.floor(100000 + Math.random() * 900000);
const message = encodeURIComponent(`Madzinu Web3: Your secure login OTP is ${otp}. Valid for 10 minutes.`);
const url = `https://www.fast2sms.com/dev/bulkV2?authorization=${apiKey}&route=q&message=${message}&language=english&flash=0&numbers=${phone}`;

console.log('🚀 Sending test request to Fast2SMS...');

https.get(url, (res) => {
    let data = '';
    res.on('data', (chunk) => { data += chunk; });
    res.on('end', () => {
        console.log('📥 Response Code:', res.statusCode);
        console.log('📥 Response Body:', data);
    });
}).on('error', (err) => {
    console.error('❌ Connection error:', err.message);
});
