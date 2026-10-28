import re

with open("routes/jobworkRoutes.js", "r", encoding="utf-8") as f:
    content = f.read()

# New live Fast2SMS integration function
fast2sms_func = """
const https = require('https');

// Helper: Send Instant Mobile SMS Alert via Fast2SMS
async function sendMobileAlert(mobileNumber, messageText) {
    const apiKey = process.env.FAST2SMS_API_KEY;
    if (!apiKey || !mobileNumber) {
        console.log('⚠️ Fast2SMS API key or mobile number missing.');
        return;
    }

    // Clean mobile number (ensure 10 digits)
    const cleanMobile = mobileNumber.replace(/[^0-9]/g, '').slice(-10);
    
    const postData = JSON.stringify({
        route: 'q',
        message: messageText,
        language: 'english',
        flash: 0,
        numbers: cleanMobile
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

    const req = https.request(options, (res) => {
        let responseBody = '';
        res.on('data', (chunk) => { responseBody += chunk; });
        res.on('end', () => {
            console.log(`📱 Fast2SMS Response for ${cleanMobile}:`, responseBody);
        });
    });

    req.on('error', (error) => {
        console.error('❌ Fast2SMS Dispatch Error:', error);
    });

    req.write(postData);
    req.end();
}
"""

# Replace the old placeholder sendMobileAlert function
content = re.sub(r'async function sendMobileAlert\(.*?\n\}', fast2sms_func.strip(), content, flags=re.DOTALL)

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated routes/jobworkRoutes.js with live Fast2SMS integration!")
