import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    name: { type: String },
    createdAt: { type: Date, default: Date.now }
});

const JobworkLedgerSchema = new mongoose.Schema({
    orderId: { type: String, required: true, unique: true },
    clientEmail: { type: String, required: true },
    specification: { type: String },
    amount: { type: Number, required: true },
    ipAddress: { type: String },
    status: { type: String, default: 'Completed' },
    createdAt: { type: Date, default: Date.now }
});

const PayoutSchema = new mongoose.Schema({
    orderId: { type: String },
    amount: { type: Number },
    status: { type: String, default: 'Pending' },
    createdAt: { type: Date, default: Date.now }
});

export const User = mongoose.models.User || mongoose.model('User', UserSchema);
export const JobworkLedger = mongoose.models.JobworkLedger || mongoose.model('JobworkLedger', JobworkLedgerSchema);
export const Payout = mongoose.models.Payout || mongoose.model('Payout', PayoutSchema);
