with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the Penny Drop script & modal with a clean save form
clean_bank_modal_and_js = """
    <!-- Bank Details Entry Modal -->
    <div id="bank-details-modal" class="modal-overlay">
        <div class="modal-content" style="border-color: #3b82f6;">
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
            <button onclick="saveBankDetailsOnly()" class="admin-btn-action" style="width: 100%; padding: 10px; background: #10b981;">Save Bank Details for Admin Payout</button>
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

        document.getElementById('user-bank-display-box').innerHTML = `
            <div style="color: #34d399; font-weight: bold;">✓ SAVED FOR ADMIN PAYOUT</div>
            <div>Name: <b>${name || 'Holder'}</b></div>
            <div>Acc/UPI: <b>${acc ? '•••• ' + acc.slice(-4) : upi}</b> | IFSC: <b>${ifsc || 'N/A'}</b></div>
        `;

        closeBankDetailsModal();
        alert('Bank details successfully saved! Admin can now view this for payouts.');
    }
</script>
"""

# Replace old modal/script block in index.html
if "verifyAndSaveBankDetails" in content:
    # Find and replace old script block
    start_idx = content.find("<!-- Bank Details Entry & Penny Drop Modal -->")
    if start_idx == -1:
        start_idx = content.find("<div id=\"bank-details-modal\"")
    
    end_idx = content.find("</script>", start_idx)
    end_idx = content.find("</script>", end_idx + 9) # find end of second script tag if any
    
    if start_idx != -1:
        content = content[:start_idx] + clean_bank_modal_and_js
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully removed Penny Drop and updated simple bank save!")
    else:
        print("Could not locate precise index. Please check content.")
else:
    print("Bank modal not found to replace.")
