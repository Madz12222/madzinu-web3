import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import dotenv from 'dotenv';
import jobworkRoutes from './routes/jobworkRoutes.js';

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Connect to MongoDB if URI is available
if (process.env.MONGO_URI) {
    mongoose.connect(process.env.MONGO_URI)
        .then(() => console.log('✅ MongoDB connected'))
        .catch(err => console.error('❌ MongoDB error:', err));
}

// API Routes
app.use('/api', jobworkRoutes);

if (process.env.NODE_ENV !== 'production') {
    const PORT = process.env.PORT || 5000;
    app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
}

export default app;

// Backend OTP Dispatch Route via Fast2SMS
app.post('/api/send-otp', async (req, res) => {
    const { phone } = req.body;
    if (!phone) {
        return res.status(400).json({ success: false, message: 'Phone number is required' });
    }

    const otp = Math.floor(100000 + Math.random() * 900000);
    const apiKey = process.env.FAST2SMS_API_KEY;
    const message = encodeURIComponent(`Madzinu Web3: Your secure login OTP is ${otp}. Valid for 10 minutes.`);
    const formattedPhone = phone.startsWith('91') ? phone : `91${phone}`;
    const url = `https://www.fast2sms.com/dev/bulkV2?authorization=${apiKey}&route=q&message=${message}&language=english&flash=0&numbers=${formattedPhone}`;

    https.get(url, (smsRes) => {
        let data = '';
        smsRes.on('data', (chunk) => { data += chunk; });
        smsRes.on('end', () => {
            try {
                const responseJson = JSON.parse(data);
                if (responseJson.return) {
                    console.log(`✅ OTP ${otp} sent successfully to ${formattedPhone}`);
                    res.json({ success: true, message: 'OTP sent successfully!' });
                } else {
                    res.status(500).json({ success: false, message: 'Failed to send SMS via Fast2SMS', details: responseJson });
                }
            } catch (e) {
                res.status(500).json({ success: false, message: 'Invalid response from SMS gateway' });
            }
        });
    }).on('error', (err) => {
        console.error('❌ Fast2SMS Error:', err);
        res.status(500).json({ success: false, message: 'Internal server error while dispatching SMS' });
    });
});
