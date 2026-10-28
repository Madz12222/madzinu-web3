import dotenv from 'dotenv';
dotenv.config();
import nodemailer from 'nodemailer';
import { generateServerPlanEmail } from './templates/serverPlanEmail.js';

const SENDER_EMAIL = process.env.EMAIL_USER;
const SENDER_PASS = process.env.EMAIL_PASS;
const RECIPIENT_EMAIL = "Madzmad2222@gmail.com";

async function sendTestPlanReceipt() {
    console.log("🚀 Dispatching Server Purchase Confirmation Template...");

    const transporter = nodemailer.createTransport({
        host: 'smtp.hostinger.com',
        port: 465,
        secure: true,
        auth: {
            user: SENDER_EMAIL,
            pass: SENDER_PASS
        }
    });

    const htmlContent = generateServerPlanEmail({
        clientName: "Sampath Madhan",
        orderId: "M3W-SRV-9982",
        planName: "Hostinger Business VPS 4",
        billingCycle: "Annual (12 Months)",
        serverSpecs: {
            cpu: "8 vCPU Cores",
            ram: "16 GB RAM",
            storage: "200 GB NVMe SSD Storage",
            bandwidth: "Unmetered High-Speed Bandwidth"
        },
        amountPaid: "₹9,599.00 INR",
        ipAddress: "194.163.140.88"
    });

    try {
        const info = await transporter.sendMail({
            from: `"Madzinu Web3 Technologies" <${SENDER_EMAIL}>`,
            to: RECIPIENT_EMAIL,
            replyTo: SENDER_EMAIL,
            subject: "Server Purchase Confirmation - Order #M3W-SRV-9982",
            html: htmlContent
        });

        console.log(`✅ SERVER TEMPLATE SENT SUCCESSFULLY!`);
        console.log(`📩 Recipient: ${RECIPIENT_EMAIL}`);
        console.log(`🆔 Message ID: ${info.messageId}`);
    } catch (err) {
        console.error("❌ Failed to send template email:", err.message);
    }
}

sendTestPlanReceipt();
