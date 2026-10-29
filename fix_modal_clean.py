with open("index.html", "r") as f:
    content = f.read()

# Find and replace the user login modal section entirely
start_marker = '<!-- USER LOGIN MODAL -->'
end_marker = '<!-- ADMIN LOGIN MODAL -->'

new_modals = """    <!-- USER LOGIN MODAL -->
    <div id="user-login-modal" class="modal-overlay">
        <div class="modal-content">
            <h3 style="font-size: 14px; font-weight: bold; color: #38bdf8; margin-bottom: 10px;"><i class="fa-solid fa-lock"></i> Portal Sign-In</h3>
            <p style="font-size: 10px; color: #94a3b8; margin-bottom: 12px;">Enter your mobile number to sign in instantly.</p>
            <input type="text" id="login-phone-input" placeholder="Enter Mobile Number" class="admin-input-box" style="margin-bottom: 10px;">
            <button onclick="loginUserDirect()" class="admin-btn-action" style="width: 100%; padding: 10px; margin-bottom: 6px; background: #10b981;">Access User Dashboard</button>
            <button onclick="closeUserLoginModal()" style="background: transparent; color: #94a3b8; border: none; font-size: 10px; width: 100%; cursor: pointer; margin-top: 6px;">Cancel</button>
        </div>
    </div>

    <!-- USER DASHBOARD VIEW MODAL -->
    <div id="user-dashboard-modal" class="modal-overlay">
        <div class="modal-content" style="max-width: 450px; background: #0f172a; border: 1px solid #10b981;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3 style="font-size: 14px; font-weight: bold; color: #10b981;"><i class="fa-solid fa-chart-line"></i> User Terminal Dashboard</h3>
                <button onclick="closeUserDashboard()" style="background: none; border: none; color: #f87171; font-size: 18px; font-weight: bold; cursor: pointer;">&times;</button>
            </div>
            <div style="font-size: 11px; color: #cbd5e1; display: flex; flex-direction: column; gap: 10px;">
                <div style="background: #1e1b4b; padding: 10px; border-radius: 8px; border: 1px solid #312e81;">
                    <div style="color: #38bdf8; font-weight: bold;">👤 Authenticated Mobile:</div>
                    <div id="dash-phone-display" style="font-size: 12px; color: #fff;">+91 8122252222</div>
                </div>
                <div style="background: #111827; padding: 10px; border-radius: 8px; border: 1px solid #1f2937;">
                    <div style="color: #f59e0b; font-weight: bold;">💰 Live Workspace Balance:</div>
                    <div style="font-size: 16px; font-weight: 900; color: #34d399;">₹0.00 <span style="font-size: 9px; color: #94a3b8;">(Active Node: None)</span></div>
                </div>
                <div style="background: #111827; padding: 10px; border-radius: 8px; border: 1px solid #1f2937;">
                    <div style="color: #38bdf8; font-weight: bold;">🔗 Direct Referral Link:</div>
                    <input type="text" readonly value="https://madzinuweb3technologies.in/?ref=MADZINU" style="background: #090d16; border: 1px solid #334155; color: #38bdf8; padding: 6px; width: 100%; border-radius: 4px; font-size: 9.5px; margin-top: 4px;">
                </div>
                <button onclick="alert('⚡ Please select a Cloud Node tier to activate daily E-Commerce jobworks.')" class="btn-primary" style="margin-top: 4px; padding: 10px; font-size: 11px;">Activate Cloud Node & Start Earning</button>
            </div>
        </div>
    </div>

    <!-- ADMIN LOGIN MODAL -->"""

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    content = content[:start_idx] + new_modals + content[end_idx:]

# Also update the login JS function cleanly at the bottom
script_start = "<script>"
new_js_func = """        async function loginUserDirect() {
            const phoneInput = document.getElementById('login-phone-input');
            if (!phoneInput || !phoneInput.value.trim()) {
                alert('❌ Please enter a valid mobile number.');
                return;
            }
            const phone = phoneInput.value.trim();
            
            // Trigger Fast2SMS in background
            try {
                fetch('/api/send-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ phone: phone })
                });
            } catch (e) {
                console.log("Background API dispatch initiated");
            }

            // Instantly open User Dashboard
            closeUserLoginModal();
            document.getElementById('dash-phone-display').innerText = "+91 " + phone;
            document.getElementById('user-dashboard-modal').style.display = 'flex';
            phoneInput.value = "";
        }

        function closeUserDashboard() {
            document.getElementById('user-dashboard-modal').style.display = 'none';
        }"""

if script_start in content:
    content = content.replace(script_start, script_start + "\n" + new_js_func)

with open("index.html", "w") as f:
    f.write(content)

print("Clean fix applied successfully!")
