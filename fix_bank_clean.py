with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove any old incomplete modal if present
if "bank-details-modal" in content:
    # Let's strip out the old modal section to prevent duplicates
    import re
    content = re.sub(r'<!-- Bank Details.*?<\/div>\s*<\/div>\s*<\/div>', '', content, flags=re.DOTALL)

simple_bank_system = """
    <!-- Bank Details Entry Modal -->
    <div id="bank-details-modal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 99999; justify-content: center; align-items: center;">
        <div class="modal-content" style="background: #111827; border: 1px solid #3b82f6; padding: 20px; border-radius: 14px; width: 90%; max-width: 400px; text-align: left;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #1f2937; padding-bottom: 8px;">
                <span style="font-weight: bold; color: #38bdf8; font-size: 13px;">Save Payout Bank Details</span>
                <button onclick="closeBankDetailsModal()" style="background: none; border: none; color: #94a3b8; font-size: 18px; cursor: pointer;">&times;</button>
            </div>
            <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 10px;">
                <input type="text" id="bank-acc-holder" placeholder="Account Holder Legal Name" class="admin-input-box">
                <input type="text" id="bank-acc-num" placeholder="Bank Account Number" class="admin-input-box">
                <input type="text" id="bank-ifsc" placeholder="IFSC Code (e.g. SBIN0001234)" class="admin-input-box">
                <input type="text" id="bank-upi-id" placeholder="UPI ID (e.g. mobile@paytm / name@upi)" class="admin-input-box">
            </div>
            <button onclick="saveBankDetailsOnly()" class="admin-btn-action" style="width: 100%; padding: 10px; background: #10b981; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer;">Save Bank Details for Admin Payout</button>
        </div>
    </div>

<script>
    function openBankDetailsModal() { document.getElementById('bank-details-modal').style.display = 'flex'; }
    function closeBankDetailsModal() { document.getElementById('bank-details-modal').style.display = 'none'; }

    function saveBankDetailsOnly() {
        let name = document.getElementById('bank-acc-holder').value.trim();
        let acc = document.getElementById('bank-acc-num').value.trim();
        let ifsc = document.getElementById('bank-ifsc').value.trim();
        let upi = document.getElementById('bank-upi-id').value.trim();

        if(!acc && !upi) {
            alert('Please enter either a Bank Account + IFSC or a valid UPI ID!');
            return;
        }

        let activeMobile = document.getElementById('user-mobile-display').innerText.replace('+91 ', '').trim();
        
        if(!platformData.userStore[activeMobile]) {
            platformData.userStore[activeMobile] = { inrBal: 0, goldGrams: 0, silverGrams: 0 };
        }

        platformData.userStore[activeMobile].bankDetails = {
            name: name || "Contractor",
            accountNumber: acc,
            ifsc: ifsc,
            upiId: upi
        };

        let displayBox = document.getElementById('user-bank-display-box');
        if(displayBox) {
            displayBox.innerHTML = `
                <div style="color: #34d399; font-weight: bold;">✓ SAVED FOR ADMIN PAYOUT</div>
                <div>Name: <b>${name || 'Holder'}</b></div>
                <div>Acc/UPI: <b>${acc ? '•••• ' + acc.slice(-4) : upi}</b> | IFSC: <b>${ifsc || 'N/A'}</b></div>
            `;
        }

        closeBankDetailsModal();
        alert('Bank details successfully saved! Admin can now view this for payouts.');
    }
</script>
"""

content = content.replace("</body>", simple_bank_system + "\n</body>")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully added clean bank details modal and saving logic!")
