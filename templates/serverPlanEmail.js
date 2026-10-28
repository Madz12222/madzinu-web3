export const generateServerPlanEmail = (data) => {
    const {
        clientName = "Valued Partner",
        orderId = "ORD-" + Math.floor(100000 + Math.random() * 900000),
        planName = "Enterprise Cloud VPS II",
        billingCycle = "Annual",
        serverSpecs = {
            cpu: "4 vCPU Cores",
            ram: "8 GB RAM",
            storage: "100 GB NVMe SSD",
            bandwidth: "Unmetered 1 Gbps"
        },
        amountPaid = "₹4,999.00",
        ipAddress = "194.163.140.88",
        activationDate = new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })
    } = data;

    return `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Server Plan Activation Receipt</title>
    </head>
    <body style="margin:0; padding:0; background-color:#f4f6f9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
      <table border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;">
        <tr>
          <td align="center" style="padding: 20px 0;">
            <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08);">
              
              <!-- Header -->
              <tr>
                <td align="center" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 35px 20px;">
                  <h1 style="color:#38bdf8; margin:0; font-size:26px; font-weight:700; letter-spacing:1px;">Madzinu Web3 Technologies</h1>
                  <p style="color:#94a3b8; margin:5px 0 0 0; font-size:14px;">Enterprise Cloud & Infrastructure Services</p>
                </td>
              </tr>

              <!-- Sub-header Badge -->
              <tr>
                <td style="padding: 25px 30px 10px 30px;">
                  <div style="background-color:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:12px 15px; text-align:center;">
                    <span style="color:#059669; font-weight:700; font-size:15px;">🎉 Server Plan Activated Successfully!</span>
                  </div>
                </td>
              </tr>

              <!-- Greeting & Info -->
              <tr>
                <td style="padding: 10px 30px; color:#334155; font-size:15px; line-height:1.6;">
                  <p style="margin:0;">Hello <strong>${clientName}</strong>,</p>
                  <p style="margin:10px 0 0 0;">Thank you for your business. Your server instance has been provisioned and is now fully active on the Madzinu Web3 network.</p>
                </td>
              </tr>

              <!-- Order Summary Table -->
              <tr>
                <td style="padding: 15px 30px;">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:15px;">
                    <tr>
                      <td style="padding: 5px 0; color:#64748b; font-size:13px;">Order ID:</td>
                      <td align="right" style="padding: 5px 0; color:#0f172a; font-weight:600; font-size:13px;">${orderId}</td>
                    </tr>
                    <tr>
                      <td style="padding: 5px 0; color:#64748b; font-size:13px;">Activation Date:</td>
                      <td align="right" style="padding: 5px 0; color:#0f172a; font-weight:600; font-size:13px;">${activationDate}</td>
                    </tr>
                    <tr>
                      <td style="padding: 5px 0; color:#64748b; font-size:13px;">Billing Cycle:</td>
                      <td align="right" style="padding: 5px 0; color:#0f172a; font-weight:600; font-size:13px;">${billingCycle}</td>
                    </tr>
                    <tr>
                      <td style="padding: 5px 0; color:#64748b; font-size:13px; font-weight:700;">Total Paid:</td>
                      <td align="right" style="padding: 5px 0; color:#0284c7; font-weight:700; font-size:16px;">${amountPaid}</td>
                    </tr>
                  </table>
                </td>
              </tr>

              <!-- Server Specs Card -->
              <tr>
                <td style="padding: 10px 30px;">
                  <h3 style="color:#0f172a; margin:0 0 12px 0; font-size:16px; border-left:4px solid #0284c7; padding-left:10px;">📦 Purchased Plan Specifications</h3>
                  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                      <td style="padding: 10px 0; color:#475569; font-size:14px;"><strong>Selected Plan:</strong></td>
                      <td align="right" style="padding: 10px 0; color:#0f172a; font-weight:700; font-size:14px;">${planName}</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                      <td style="padding: 10px 0; color:#475569; font-size:14px;">Processor (CPU):</td>
                      <td align="right" style="padding: 10px 0; color:#334155; font-size:14px;">${serverSpecs.cpu}</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                      <td style="padding: 10px 0; color:#475569; font-size:14px;">Memory (RAM):</td>
                      <td align="right" style="padding: 10px 0; color:#334155; font-size:14px;">${serverSpecs.ram}</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #f1f5f9;">
                      <td style="padding: 10px 0; color:#475569; font-size:14px;">Storage (NVMe SSD):</td>
                      <td align="right" style="padding: 10px 0; color:#334155; font-size:14px;">${serverSpecs.storage}</td>
                    </tr>
                    <tr>
                      <td style="padding: 10px 0; color:#475569; font-size:14px;">Network Speed:</td>
                      <td align="right" style="padding: 10px 0; color:#334155; font-size:14px;">${serverSpecs.bandwidth}</td>
                    </tr>
                  </table>
                </td>
              </tr>

              <!-- Server IP Box -->
              <tr>
                <td style="padding: 15px 30px;">
                  <div style="background-color:#0f172a; border-radius:8px; padding:15px; text-align:center;">
                    <span style="color:#94a3b8; font-size:12px; display:block; text-transform:uppercase; letter-spacing:1px;">Assigned Dedicated IP Address</span>
                    <span style="color:#38bdf8; font-family:monospace; font-size:20px; font-weight:700; margin-top:5px; display:block;">${ipAddress}</span>
                  </div>
                </td>
              </tr>

              <!-- Action Button -->
              <tr>
                <td align="center" style="padding: 20px 30px 30px 30px;">
                  <a href="https://madzinuweb3technologies.in" target="_blank" style="background-color:#0284c7; color:#ffffff; text-decoration:none; padding:14px 30px; border-radius:6px; font-weight:700; font-size:15px; display:inline-block; box-shadow: 0 4px 10px rgba(2,132,199,0.3);">Access Server Console</a>
                </td>
              </tr>

              <!-- Footer -->
              <tr>
                <td style="background-color:#f8fafc; padding:20px 30px; border-top:1px solid #e2e8f0; text-align:center; color:#94a3b8; font-size:12px; line-height:1.5;">
                  <p style="margin:0;">Madzinu Web3 Technologies • Enterprise Jobwork & Server Division</p>
                  <p style="margin:5px 0 0 0;">Need support? Contact us at <a href="mailto:support@madzinuweb3technologies.in" style="color:#0284c7; text-decoration:none;">support@madzinuweb3technologies.in</a></p>
                </td>
              </tr>

            </table>
          </td>
        </tr>
      </table>
    </body>
    </html>
    `;
};
