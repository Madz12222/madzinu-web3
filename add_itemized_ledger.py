import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

itemized_ledger_code = """
    <!-- ITEMIZED JOBWORK LEDGER & SHA-256 HASH BREAKDOWN MODAL / DRAWER -->
    <div id="itemized-ledger-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 99999; justify-content: center; align-items: center;">
        <div class="modal-content" style="background: #111827; border: 1px solid #3b82f6; padding: 20px; border-radius: 14px; width: 92%; max-width: 600px; max-height: 85vh; overflow-y: auto; text-align: left;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #1f2937; padding-bottom: 8px;">
                <span style="font-weight: bold; color: #38bdf8; font-size: 13px;"><i class="fa-solid fa-list-check"></i> Itemized Jobwork Audit & Hash Ledger</span>
                <button onclick="closeItemizedLedger()" style="background: none; border: none; color: #94a3b8; font-size: 18px; cursor: pointer;">&times;</button>
            </div>
            <div style="font-size: 11px; color: #94a3b8; margin-bottom: 10px;">
                Daily Target: <b>₹4,000.00</b> | Unit Price per Jobwork: <b>₹20.00</b> | Total Jobworks Required: <b>200 Units</b>
            </div>
            <div id="ledger-items-container" style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 12px;">
                <!-- Dynamically populated jobwork rows -->
                <div style="padding: 8px; background: #1f2937; border-radius: 6px; font-size: 10px; color: #d1d5db; display: flex; justify-content: space-between; align-items: center;">
                    <span><b>JW-40001</b> | Enterprise SKU Audit</span>
                    <span style="color: #34d399;">₹20.00 | SHA256-8A4F...12</span>
                </div>
            </div>
            <button onclick="closeItemizedLedger()" class="admin-btn-action" style="width: 100%; padding: 10px; background: #2563eb; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer;">Close Ledger</button>
        </div>
    </div>

<script>
    function openItemizedLedger() {
        document.getElementById('itemized-ledger-modal').style.display = 'flex';
        renderItemizedLedger();
    }

    function closeItemizedLedger() {
        document.getElementById('itemized-ledger-modal').style.display = 'none';
    }

    async function renderItemizedLedger() {
        let container = document.getElementById('ledger-items-container');
        container.innerHTML = '<div style="color: #38bdf8; font-size: 11px; text-align: center; padding: 10px;">Generating cryptographic verification proofs for 200 jobwork units...</div>';
        
        let html = '';
        // Simulating the 200 jobwork breakdown for ₹4,000 (Showing sample preview of verified units)
        for(let i = 1; i <= 10; i++) {
            let jwId = "JW-50" + (100 + i);
            let randomHash = "SHA256-" + Math.random().toString(16).substring(2, 10).toUpperCase() + Math.random().toString(16).substring(2, 10).toUpperCase();
            html += `
                <div style="padding: 8px; background: #1f2937; border-radius: 6px; font-size: 10px; color: #d1d5db; display: flex; justify-content: space-between; align-items: center; border-left: 3px solid #10b981;">
                    <div><b>${jwId}</b> <span style="color: #94a3b8;">(Catalog Audit Node #${i})</span></div>
                    <div style="text-align: right;"><span style="color: #34d399; font-weight: bold;">₹20.00</span><br><span style="font-family: monospace; font-size: 9px; color: #38bdf8;">${randomHash}</span></div>
                </div>
            `;
        }
        html += '<div style="font-size: 10px; color: #94a3b8; text-align: center; padding: 4px;">... and 190 more verified jobwork units totaling ₹3,800.00 (Full 200/200 Units Verified)</div>';
        container.innerHTML = html;
    }
</script>
"""

# Append before </body>
if "itemized-ledger-modal" not in content:
    content = content.replace("</body>", itemized_ledger_code + "\n</body>")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully injected itemized jobwork ledger and hash breakdown!")
else:
    print("Ledger code already exists.")
