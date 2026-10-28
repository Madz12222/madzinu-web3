import { generateServerPlanEmail } from '../templates/serverPlanEmail.js';
import express from 'express';
import crypto from 'crypto';
import nodemailer from 'nodemailer';
import { User, JobworkLedger, Payout } from '../models/Schema.js';
const router = express.Router();

// Configure Email Transporter (Gmail / Enterprise SMTP)
const transporter = nodemailer.createTransport({
    host: 'smtp.hostinger.com',
    port: 465,
    secure: true,
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    }
});

// Helper: Send Instant Email Receipt
async function sendEmailReceipt(userEmail, userName, title, messageBody) {
    if (!userEmail) return;
    try {
        await transporter.sendMail({
            from: '"Madzinu Enterprise Node Platform" <support@madzinuweb3technologies.in>',
            to: userEmail,
            subject: `[Madzinu Enterprise] ${title}`,
            text: `Dear ${userName || 'Contractor'},

${messageBody}

Check your dashboard for itemized SHA-256 audit hashes and ledger history.

Madzinu Web3 Technologies`
        });
        console.log(`✅ Email receipt sent to ${userEmail}`);
    } catch (err) {
        console.error(`❌ Email dispatch error:`, err);
    }
}

// Helper: Hook for SMS / WhatsApp Gateway (Fast2SMS / Twilio / MSG91)
import https from 'https';

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

// -------------------------------------------------------------
// 1. EXECUTE DAILY WORKLOAD & NOTIFY
// -------------------------------------------------------------
router.post('/execute-daily-workload', async (req, res) => {
    try {
        const { mobile, email, name } = req.body;
        if (!mobile) return res.status(400).json({ success: false, message: 'Mobile number required' });

        const user = await User.findOne({ mobile });
        if (!user) return res.status(404).json({ success: false, message: 'User node not found' });

        const todayStr = new Date().toISOString().split('T')[0];
        const existingExecution = await JobworkLedger.findOne({ mobile, executionDate: todayStr });
        if (existingExecution) {
            return res.status(400).json({ success: false, message: 'Daily workload already completed for today!' });
        }

        const totalUnits = user.requiredJobworks; // e.g. 200 units
        const unitPrice = user.unitPrice; // ₹20
        const ledgerEntries = [];

        for (let i = 1; i <= totalUnits; i++) {
            const jwId = `JW-${Date.now().toString().slice(-4)}${i.toString().padStart(3, '0')}`;
            const rawHash = `${mobile}-JW-${i}-${Date.now()}-${crypto.randomBytes(4).toString('hex')}`;
            const hash = 'SHA256-' + crypto.createHash('sha256').update(rawHash).digest('hex').substring(0, 24).toUpperCase();

            ledgerEntries.push({
                mobile,
                executionDate: todayStr,
                jobworkId: jwId,
                taskCategory: `Catalog Audit Node #${i}`,
                unitPrice: unitPrice,
                sha256Hash: hash,
                status: 'COMPLETED'
            });
        }

        await JobworkLedger.insertMany(ledgerEntries);
        const creditedAmount = totalUnits * unitPrice; // ₹4,000
        user.walletBalance += creditedAmount;
        await user.save();

        // Trigger Instant Notifications
        const userEmail = email || user.email;
        const msgText = `Your daily workload of ${totalUnits} enterprise units has been verified. ₹${creditedAmount} has been credited to your INR ledger.`;
        
        await sendEmailReceipt(userEmail, name || user.fullName, 'Daily Workload Credited', msgText);
        await sendMobileAlert(mobile, `Madzinu Alert: ₹${creditedAmount} credited for daily jobwork execution.`);

        return res.json({
            success: true,
            message: `Successfully processed ${totalUnits} jobwork units!`,
            creditedAmount,
            newBalance: user.walletBalance,
            sampleHash: ledgerEntries[0].sha256Hash
        });
    } catch (error) {
        console.error('Workload Error:', error);
        return res.status(500).json({ success: false, message: 'Server error processing workload' });
    }
});

// -------------------------------------------------------------
// 2. REQUEST PAYOUT & NOTIFY
// -------------------------------------------------------------
router.post('/request-payout', async (req, res) => {
    try {
        const { mobile, amount, payoutMode } = req.body;
        const user = await User.findOne({ mobile });

        if (!user || user.walletBalance < amount) {
            return res.status(400).json({ success: false, message: 'Insufficient balance' });
        }

        user.walletBalance -= amount;
        await user.save();

        const payout = new Payout({ mobile, amount, payoutMode, status: 'PENDING' });
        await payout.save();

        // Trigger Notification
        const alertMsg = `Your payout request of ₹${amount} via ${payoutMode} has been received and queued for IMPS/UPI verification.`;
        await sendEmailReceipt(user.email, user.fullName, 'Payout Request Queued', alertMsg);
        await sendMobileAlert(mobile, `Madzinu: Payout request of ₹${amount} (${payoutMode}) is pending bank verification.`);

        return res.json({
            success: true,
            message: 'Payout request queued for verification.',
            remainingBalance: user.walletBalance
        });
    } catch (error) {
        return res.status(500).json({ success: false, message: 'Error processing payout request' });
    }
});


// Dynamic Order Completion & Email Receipt Route
router.post('/complete-order', async (req, res) => {
    try {
        const { clientName, userEmail, orderDetails } = req.body; 

        if (!userEmail || !orderDetails) {
            return res.status(400).json({ success: false, error: "Missing required order payload fields." });
        }

        // Generate dynamic HTML template based on incoming user order details
        const htmlContent = generateServerPlanEmail({
            clientName: clientName || "Valued Customer",
            orderId: orderDetails.orderId || ("M3W-" + Math.floor(100000 + Math.random() * 900000)),
            planName: orderDetails.planName || "Enterprise VPS Plan",
            billingCycle: orderDetails.billingCycle || "Annual",
            serverSpecs: {
                cpu: orderDetails.cpu || "4 vCPU Cores",
                ram: orderDetails.ram || "8 GB RAM",
                storage: orderDetails.storage || "100 GB NVMe SSD",
                bandwidth: orderDetails.bandwidth || "Unmetered 1 Gbps"
            },
            amountPaid: orderDetails.price ? `₹${Number(orderDetails.price).toLocaleString('en-IN')}.00 INR` : "₹0.00 INR",
            ipAddress: orderDetails.assignedIp || "Provisioning Pending"
        });

        // Dispatch via Hostinger SMTP
        await transporter.sendMail({
            from: `"Madzinu Web3 Technologies" <${process.env.EMAIL_USER}>`,
            to: userEmail,
            replyTo: process.env.EMAIL_USER,
            subject: `Server Purchase Confirmation - Order #${orderDetails.orderId || 'SUCCESS'}`,
            html: htmlContent
        });

        console.log(`✅ Automated order receipt sent to ${userEmail}`);
        res.status(200).json({ success: true, message: "Server order processed & receipt dispatched successfully!" });
    } catch (err) {
        console.error("❌ Checkout Route Mail Error:", err.message);
        res.status(500).json({ success: false, error: err.message });
    }
});

export default router;
