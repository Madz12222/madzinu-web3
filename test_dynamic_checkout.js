import dotenv from 'dotenv';
dotenv.config();
import nodemailer from 'nodemailer';
import { generateServerPlanEmail } from './templates/serverPlanEmail.js';

const SENDER_EMAIL = process.env.EMAIL_USER;
const SENDER_PASS = process.env.EMAIL_PASS;
const RECIPIENT_EMAIL = "Madzmad2222@gmail.com";

async function testDynamicOrder() {
    console.log("🚀 Testing Dynamic Server Plan Checkout Dispatch...");

    const transporter = nodemailer.createTransport({
        host: 'smtp.hostinger.com',
        port: 465,
        secure: true,
        auth: {
            user: SENDER_EMAIL,
            pass: SENDER_PASS
        }
    });

    // Dynamic Payload Sample (Hostinger VPS 8 Plan)
    const orderDetails = {
        orderId: "M3W-SRV-4091",
        planName: "Hostinger Business VPS 8",
        billingCycle: "2 Years",
        cpu: "16 vCPU Cores",
        ram: "32 GB RAM",
        storage: "400 GB NVMe SSD Storage",
        bandwidth: "10 Gbps High-Speed",
        price: 18499,
        assignedIp: "194.163.155.99"
    };

    const htmlContent = generateServerPlanEmail({
        clientName: "Sampath Madhan",
        orderId: orderDetails.orderId,
        planName: orderDetails.planName,
        billingCycle: orderDetails.billingCycle,
        serverSpecs: {
            cpu: orderDetails.cpu,
            ram: orderDetails.ram,
            storage: orderDetails.storage,
            bandwidth: orderDetails.bandwidth
        },
        amountPaid: `₹${orderDetails.price.toLocaleString('en-IN')}.00 INR`,
        ipAddress: orderDetails.assignedIp
    });

    try {
        const info = await transporter.sendMail({
            from: `"Madzinu Web3 Technologies" <${SENDER_EMAIL}>`,
            to: RECIPIENT_EMAIL,
            replyTo: SENDER_EMAIL,
            subject: `Server Purchase Confirmation - Order #${orderDetails.orderId}`,
            html: htmlContent
        });

        console.log(`✅ DYNAMIC EMAIL SENT SUCCESSFULLY!`);
        console.log(`📩 Delivered to: ${RECIPIENT_EMAIL}`);
        console.log(`💰 Plan Price: ₹18,499.00 INR`);
        console.log(`🆔 Message ID: ${info.messageId}`);
    } catch (err) {
        console.error("❌ Failed to send dynamic email:", err.message);
    }
}

testDynamicOrder();
