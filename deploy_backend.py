import os

# Create directories if they don't exist
os.makedirs("models", exist_ok=True)
os.makedirs("routes", exist_ok=True)

# 1. Write models/Schema.js
schema_code = """const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
    mobile: { type: String, required: true, unique: true },
    fullName: { type: String, default: '' },
    bankDetails: {
        accountNumber: { type: String, default: '' },
        ifscCode: { type: String, default: '' },
        upiId: { type: String, default: '' },
        isVerified: { type: Boolean, default: false }
    },
    activeTier: { type: String, enum: ['STARTER', 'STANDARD', 'ENTERPRISE'], default: 'ENTERPRISE' },
    tierPrice: { type: Number, default: 50000 },
    dailyTargetPayout: { type: Number, default: 4000 },
    requiredJobworks: { type: Number, default: 200 },
    unitPrice: { type: Number, default: 20 },
    walletBalance: { type: Number, default: 0 },
    createdAt: { type: Date, default: Date.now }
});

const JobworkLedgerSchema = new mongoose.Schema({
    mobile: { type: String, required: true, index: true },
    executionDate: { type: String, required: true },
    jobworkId: { type: String, required: true },
    taskCategory: { type: String, default: 'Enterprise SKU Audit' },
    unitPrice: { type: Number, default: 20.00 },
    sha256Hash: { type: String, required: true },
    status: { type: String, default: 'COMPLETED' },
    timestamp: { type: Date, default: Date.now }
});

const PayoutSchema = new mongoose.Schema({
    mobile: { type: String, required: true },
    amount: { type: Number, required: true },
    payoutMode: { type: String, enum: ['IMPS', 'NEFT', 'UPI'], default: 'UPI' },
    utrNumber: { type: String, default: 'PENDING' },
    status: { type: String, enum: ['PENDING', 'VERIFIED', 'DISPATCHED', 'REJECTED'], default: 'PENDING' },
    requestedAt: { type: Date, default: Date.now }
});

module.exports = {
    User: mongoose.model('User', UserSchema),
    JobworkLedger: mongoose.model('JobworkLedger', JobworkLedgerSchema),
    Payout: mongoose.model('Payout', PayoutSchema)
};
"""

with open("models/Schema.js", "w", encoding="utf-8") as f:
    f.write(schema_code)

# 2. Write routes/jobworkRoutes.js
routes_code = """const express = require('express');
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
"""

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(routes_code)

# 3. Write server.js
server_code = """const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const jobworkRoutes = require('./routes/jobworkRoutes');

const app = express();
app.use(cors());
app.use(express.json());

const MONGO_URI = process.env.MONGO_URI || 'mongodb://127.0.0.1:27017/madzinu_audit_db';

mongoose.connect(MONGO_URI)
    .then(() => console.log('✅ MongoDB Audit Database Connected Successfully'))
    .catch(err => console.error('❌ Database Connection Error:', err));

app.use('/api/v1/jobwork', jobworkRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Enterprise Audit Server running on port ${PORT}`));
"""

with open("server.js", "w", encoding="utf-8") as f:
    f.write(server_code)

print("Successfully generated backend files: models/Schema.js, routes/jobworkRoutes.js, server.js")
