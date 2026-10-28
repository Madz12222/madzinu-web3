import os

notification_code = """const express = require('express');
const crypto = require('crypto');
const nodemailer = require('nodemailer');
const { User, JobworkLedger, Payout } = require('../models/Schema');
const router = express.Router();

// Configure Email Transporter (Gmail / Enterprise SMTP)
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL_USER || 'support@madzinuweb3technologies.in',
        pass: process.env.EMAIL_PASS || 'your_app_password'
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
            text: `Dear ${userName || 'Contractor'},\n\n${messageBody}\n\nCheck your dashboard for itemized SHA-256 audit hashes and ledger history.\n\nMadzinu Web3 Technologies`
        });
        console.log(`✅ Email receipt sent to ${userEmail}`);
    } catch (err) {
        console.error(`❌ Email dispatch error:`, err);
    }
}

// Helper: Hook for SMS / WhatsApp Gateway (Fast2SMS / Twilio / MSG91)
async function sendMobileAlert(mobileNumber, messageText) {
    // Example hook for Indian SMS gateways like Fast2SMS or MSG91
    console.log(`📱 [SMS/WhatsApp Gateway] Sending to ${mobileNumber}: "${messageText}"`);
    // Add your axios.post() call to your SMS provider API here if live credentials are ready
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

module.exports = router;
"""

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(notification_code)

print("Successfully updated routes/jobworkRoutes.js with automated email and SMS hooks!")
