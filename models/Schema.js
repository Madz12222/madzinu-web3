const mongoose = require('mongoose');

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
