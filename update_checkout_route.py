import re

with open("routes/jobworkRoutes.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure import statement is at the top
import_statement = "import { generateServerPlanEmail } from '../templates/serverPlanEmail.js';\n"
if "generateServerPlanEmail" not in content:
    content = import_statement + content

# 2. Define the complete order route code
new_route = """
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
"""

# Append the route right before export default router
if "export default router;" in content:
    content = content.replace("export default router;", new_route + "\nexport default router;")
elif "module.exports = router;" in content:
    content = content.replace("module.exports = router;", new_route + "\nmodule.exports = router;")
else:
    content += "\n" + new_route

with open("routes/jobworkRoutes.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Dynamically updated routes/jobworkRoutes.js with /complete-order route!")
