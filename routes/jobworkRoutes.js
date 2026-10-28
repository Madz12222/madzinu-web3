const express = require('express');
const crypto = require('crypto');
const { User, JobworkLedger, Payout } = require('../models/Schema');
const router = express.Router();

function generateSHA256Hash(mobile, index) {
    const rawString = `${mobile}-JW-${index}-${Date.now()}-${crypto.randomBytes(8).toString('hex')}`;
    const hashHex = crypto.createHash('sha256').update(rawString).digest('hex').toUpperCase();
    return `SHA256-${hashHex.substring(0, 24)}`;
}

router.post('/execute-daily-workload', async (req, res) => {
    try {
        const { mobile } = req.body;
        if (!mobile) return res.status(400).json({ success: false, message: 'Mobile number required' });

        const user = await User.findOne({ mobile });
        if (!user) return res.status(404).json({ success: false, message: 'User node not found' });

        const todayStr = new Date().toISOString().split('T')[0];
        const existingExecution = await JobworkLedger.findOne({ mobile, executionDate: todayStr });
        if (existingExecution) {
            return res.status(400).json({ success: false, message: 'Daily workload already completed for today!' });
        }

        const totalUnits = user.requiredJobworks;
        const unitPrice = user.unitPrice;
        const ledgerEntries = [];

        for (let i = 1; i <= totalUnits; i++) {
            const jwId = `JW-${Date.now().toString().slice(-4)}${i.toString().padStart(3, '0')}`;
            const hash = generateSHA256Hash(mobile, i);
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
        user.walletBalance += (totalUnits * unitPrice);
        await user.save();

        return res.json({
            success: true,
            message: `Successfully processed ${totalUnits} jobwork units!`,
            creditedAmount: totalUnits * unitPrice,
            newBalance: user.walletBalance,
            sampleHash: ledgerEntries[0].sha256Hash
        });
    } catch (error) {
        console.error('Workload Execution Error:', error);
        return res.status(500).json({ success: false, message: 'Server error processing workload' });
    }
});

router.get('/ledger-history/:mobile', async (req, res) => {
    try {
        const { mobile } = req.params;
        const history = await JobworkLedger.find({ mobile }).sort({ timestamp: -1 }).limit(200);
        const totalCount = await JobworkLedger.countDocuments({ mobile });
        return res.json({ success: true, totalRecords: totalCount, unitPrice: 20.00, ledger: history });
    } catch (error) {
        return res.status(500).json({ success: false, message: 'Failed to fetch ledger history' });
    }
});

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
        return res.json({ success: true, message: 'Payout request queued for verification.', remainingBalance: user.walletBalance });
    } catch (error) {
        return res.status(500).json({ success: false, message: 'Error processing payout request' });
    }
});

module.exports = router;
