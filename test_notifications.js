import dotenv from 'dotenv';
dotenv.config();
import nodemailer from 'nodemailer';
import https from 'https';

const SENDER_EMAIL = process.env.EMAIL_USER;
const SENDER_PASS = process.env.EMAIL_PASS;
const RECIPIENT_EMAIL = "madhansam2222@gmail.com";
const TEST_MOBILE = "8122252222";

console.log(`🚀 Testing Hostinger SMTP for: ${SENDER_EMAIL} ...\n`);

async function testEmail() {
    console.log("📧 Testing Hostinger Direct Mail Dispatch...");
    if (!SENDER_EMAIL || !SENDER_PASS) {
        console.error("❌ EMAIL_USER or EMAIL_PASS missing in .env!");
        return;
    }

    const transporter = nodemailer.createTransport({
        host: 'smtp.hostinger.com',
        port: 465,
        secure: true, // SSL
        auth: {
            user: SENDER_EMAIL,
            pass: SENDER_PASS
        }
    });

    try {
        const info = await transporter.sendMail({
            from: `"Madzinu Web3 Technologies" <${SENDER_EMAIL}>`,
            to: RECIPIENT_EMAIL,
            replyTo: SENDER_EMAIL,
            subject: "[TEST] Official Enterprise Dispatch - Madzinu Web3",
            html: `
              <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
                <h2 style="color: #0047AB;">Madzinu Web3 Technologies</h2>
                <p>Hello Sampath,</p>
                <p>This is a live test email sent directly via your corporate Hostinger SMTP server.</p>
                <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;" />
                <p style="font-size: 12px; color: #777;">Sender: <strong>${SENDER_EMAIL}</strong></p>
              </div>
            `
        });
        console.log(`✅ HOSTINGER EMAIL SUCCESS! Sent to ${RECIPIENT_EMAIL}. Message ID: ${info.messageId}\n`);
    } catch (err) {
        console.error(`❌ Email Failed:`, err.message, "\n");
    }
}

async function testSMS() {
    console.log("📱 Testing Fast2SMS Mobile Text Dispatch...");
    const apiKey = process.env.FAST2SMS_API_KEY;
    if (!apiKey) {
        console.error("❌ FAST2SMS_API_KEY missing in .env!");
        return;
    }

    const postData = JSON.stringify({
        route: 'q',
        message: 'Madzinu Alert: Corporate notification engine active!',
        language: 'english',
        flash: 0,
        numbers: TEST_MOBILE
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
        let body = '';
        res.on('data', (chunk) => { body += chunk; });
        res.on('end', () => {
            console.log(`📱 Fast2SMS Response:`, body, "\n");
        });
    });

    req.on('error', (err) => {
        console.error('❌ SMS Request Failed:', err.message, "\n");
    });

    req.write(postData);
    req.end();
}

(async () => {
    await testEmail();
    await testSMS();
})();
