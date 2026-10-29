import nodemailer from 'nodemailer';
import dotenv from 'dotenv';

dotenv.config();

const transporter = nodemailer.createTransport({
    host: 'smtp.hostinger.com',
    port: 465,
    secure: true,
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    }
});

async function sendTest() {
    try {
        console.log('Sending fully responsive HTML receipt...');
        const info = await transporter.sendMail({
            from: `"Madzinu Web3 Technologies" <${process.env.EMAIL_USER}>`,
            to: 'madzmad2222@gmail.com',
            subject: 'Server Plan Activated Successfully - M3W-SRV-9982',
            html: `
            <div style="font-family: Arial, sans-serif; background-color: #f4f7f6; padding: 10px; width: 100%; box-sizing: border-box;">
                <div style="max-width: 100%; width: 100%; margin: 0 auto; background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
                    <div style="background: #0f172a; color: #ffffff; padding: 20px; text-align: center;">
                        <h1 style="margin: 0; font-size: 20px; color: #38bdf8;">Madzinu Web3 Technologies</h1>
                        <p style="margin: 5px 0 0; color: #94a3b8; font-size: 12px;">Enterprise Cloud & Infrastructure Services</p>
                    </div>
                    <div style="padding: 15px;">
                        <div style="background: #e2f8f0; color: #065f46; padding: 10px 15px; border-radius: 6px; font-weight: bold; font-size: 14px; margin-bottom: 15px;">
                            🎉 Server Plan Activated Successfully!
                        </div>
                        <p style="color: #334155; font-size: 14px;">Hello <strong>Sampath Madhan</strong>,</p>
                        <p style="color: #475569; font-size: 13px; line-height: 1.4;">Thank you for your business. Your server instance has been provisioned and is now fully active on the Madzinu Web3 network.</p>
                        
                        <table style="width: 100%; border-collapse: collapse; margin: 15px 0; background: #f8fafc; border-radius: 6px; font-size: 13px;">
                            <tr><td style="padding: 10px; border-bottom: 1px solid #e2e8f0; color: #64748b;">Order ID:</td><td style="padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: right; font-weight: bold; color: #0f172a; word-break: break-all;">M3W-SRV-9982</td></tr>
                            <tr><td style="padding: 10px; border-bottom: 1px solid #e2e8f0; color: #64748b;">Activation Date:</td><td style="padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: right; font-weight: bold; color: #0f172a;">28 Oct 2026</td></tr>
                            <tr><td style="padding: 10px; border-bottom: 1px solid #e2e8f0; color: #64748b;">Billing Cycle:</td><td style="padding: 10px; border-bottom: 1px solid #e2e8f0; text-align: right; font-weight: bold; color: #0f172a;">Annual (12 Months)</td></tr>
                            <tr><td style="padding: 10px; color: #64748b;">Total Paid:</td><td style="padding: 10px; text-align: right; font-weight: bold; color: #0284c7; font-size: 15px;">₹9,599.00 INR</td></tr>
                        </table>

                        <h3 style="color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px; margin-top: 20px; font-size: 15px;">📦 Plan Specifications</h3>
                        <table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #334155;">
                            <tr><td style="padding: 8px 0; border-bottom: 1px solid #f1f5f9;"><strong>Selected Plan:</strong></td><td style="text-align: right; border-bottom: 1px solid #f1f5f9;">Hostinger Business VPS 4</td></tr>
                            <tr><td style="padding: 8px 0; border-bottom: 1px solid #f1f5f9;"><strong>Processor (CPU):</strong></td><td style="text-align: right; border-bottom: 1px solid #f1f5f9;">8 vCPU Cores</td></tr>
                            <tr><td style="padding: 8px 0; border-bottom: 1px solid #f1f5f9;"><strong>Memory (RAM):</strong></td><td style="text-align: right; border-bottom: 1px solid #f1f5f9;">16 GB RAM</td></tr>
                            <tr><td style="padding: 8px 0; border-bottom: 1px solid #f1f5f9;"><strong>Storage (NVMe SSD):</strong></td><td style="text-align: right; border-bottom: 1px solid #f1f5f9;">200 GB NVMe SSD</td></tr>
                        </table>
                    </div>
                    <div style="background: #f1f5f9; padding: 15px; text-align: center; color: #64748b; font-size: 11px;">
                        &copy; 2026 Madzinu Web3 Technologies. All rights reserved.
                    </div>
                </div>
            </div>
            `
        });
        console.log('✅ Responsive email sent successfully! Message ID:', info.messageId);
    } catch (error) {
        console.error('❌ Error sending email:', error);
    }
}

sendTest();
