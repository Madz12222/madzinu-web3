with open("index.html", "r") as f:
    content = f.read()

# Strip everything from the accidental code leakage point onwards
if "function renderDashboard" in content:
    content = content.split("function renderDashboard")[0]

# Ensure we cleanly append closing tags and a properly encapsulated script block
clean_ending = """    <script>
        function renderDashboard(mobile) {
            const currentBal = localStorage.getItem('balance_' + mobile) || '100';
            const container = document.querySelector('.container');
            container.innerHTML = `
                <div class="section-box" style="border: 1px solid #10b981;">
                    <h3 style="color: #34d399; font-size: 13px;"><i class="fa-solid fa-user-check"></i> User Dashboard</h3>
                    <p style="margin-top: 6px;">Connected Mobile: <strong>${mobile}</strong></p>
                    <p>Wallet Balance: <strong style="color: #f59e0b; font-size: 14px;">₹${currentBal}</strong></p>
                    <div style="margin-top: 10px; display: flex; gap: 8px;">
                        <button onclick="openMailAccessInbox('${mobile}')" style="flex: 1; background: #0284c7; color: #fff; border: none; padding: 8px; border-radius: 6px; font-weight: bold; cursor: pointer;"><i class="fa-solid fa-envelope"></i> Mail Inbox Access</button>
                        <button onclick="location.reload()" style="background: #ef4444; color: #fff; border: none; padding: 8px 12px; border-radius: 6px; font-weight: bold; cursor: pointer;">Logout</button>
                    </div>
                </div>
            `;
        }

        function openMailAccessInbox(mobile) {
            const container = document.querySelector('.container');
            container.innerHTML += `
                <div class="section-box" style="margin-top: 10px; border: 1px solid #0284c7;">
                    <h4 style="color: #38bdf8; font-size: 12px;"><i class="fa-solid fa-inbox"></i> Secure Mail Access Inbox (${mobile})</h4>
                    <p style="font-size: 10px; color: #94a3b8; margin-top: 4px;">Incoming system verification & server node notifications:</p>
                    <div style="background: #090d16; padding: 8px; border-radius: 6px; margin-top: 8px; font-size: 10px;">
                        <div style="color: #34d399; font-weight: bold;">[Govt MeitY Startup Verification]</div>
                        <div>Node compute session active for ${mobile}. Secure API sync verified.</div>
                    </div>
                    <button onclick="renderDashboard('${mobile}')" style="margin-top: 10px; background: #334155; color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 10px;">Back to Dashboard</button>
                </div>
            `;
        }

        function openAdminLoginModal() {
            const pwd = prompt('Enter Admin Password:');
            if(pwd === 'madzinu2026') {
                renderAdminDashboard();
            } else if(pwd !== null) {
                alert('Incorrect Password!');
            }
        }

        function renderAdminDashboard() {
            const container = document.querySelector('.container');
            container.innerHTML = `
                <div class="section-box" style="border: 1px solid #f43f5e;">
                    <h3 style="color: #fb7185; font-size: 13px;"><i class="fa-solid fa-user-shield"></i> Admin Backend Control Panel</h3>
                    <p style="font-size: 10.5px; color: #94a3b8; margin-top: 4px;">Instantly alter any user wallet balance, node tier, or rewards by mobile number.</p>
                    
                    <div style="margin-top: 12px; display: flex; flex-direction: column; gap: 8px;">
                        <input type="text" id="admin-target-mobile" placeholder="Target Mobile Number (10 digits)" style="background: #090d16; border: 1px solid #334155; padding: 8px; border-radius: 8px; color: #fff; font-size: 11px;">
                        <input type="number" id="admin-new-amount" placeholder="New Balance / Amount (₹)" style="background: #090d16; border: 1px solid #334155; padding: 8px; border-radius: 8px; color: #fff; font-size: 11px;">
                        <button onclick="adminAlterUserBalance()" style="background: #e11d48; color: #fff; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 11px;">Update User Wallet / Balance Instantly</button>
                    </div>
                    <button onclick="location.reload()" style="margin-top: 12px; background: #334155; color: #fff; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 10.5px;">Exit Admin Panel</button>
                </div>
            `;
        }

        function adminAlterUserBalance() {
            const mobile = document.getElementById('admin-target-mobile').value.trim();
            const newAmount = document.getElementById('admin-new-amount').value.trim();

            if (!mobile || mobile.length < 10) {
                alert('Please enter a valid target mobile number.');
                return;
            }
            if (!newAmount) {
                alert('Please enter the amount to set.');
                return;
            }

            localStorage.setItem('balance_' + mobile, newAmount);
            alert('Successfully updated wallet balance for mobile ' + mobile + ' to ₹' + newAmount);
        }
    </script>
</body>
</html>
"""

# Append the clean closing block properly
if not content.strip().endswith("</html>"):
    content += "\n" + clean_ending

with open("index.html", "w") as f:
    f.write(content)

print("Code leakage fixed successfully!")
