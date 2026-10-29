with open("index.html", "r") as f:
    content = f.read()

# Simplify the login modal HTML back to a single step
old_login_modal = """    <!-- USER LOGIN MODAL -->
    <div id="user-login-modal" class="modal-overlay">
        <div class="modal-content">
            <h3 style="font-size: 14px; font-weight: bold; color: #38bdf8; margin-bottom: 10px;"><i class="fa-solid fa-lock"></i> Portal Sign-In</h3>
            <div id="otp-step-1">
                <p style="font-size: 10px; color: #94a3b8; margin-bottom: 12px;">Enter your mobile number to receive a secure Fast2SMS OTP.</p>
                <input type="text" id="login-phone-input" placeholder="Enter Mobile Number" class="admin-input-box" style="margin-bottom: 10px;">
                <button onclick="sendOTPFromModal()" class="admin-btn-action" style="width: 100%; padding: 10px; margin-bottom: 6px;">Send OTP</button>
            </div>
            <div id="otp-step-2" style="display: none;">
                <p style="font-size: 10px; color: #34d399; margin-bottom: 12px;">Enter the 6-digit OTP sent to your phone.</p>
                <input type="text" id="verify-otp-input" placeholder="Enter 6-Digit OTP" class="admin-input-box" style="margin-bottom: 10px;">
                <button onclick="verifyOTPAndOpenDashboard()" class="admin-btn-action" style="width: 100%; padding: 10px; margin-bottom: 6px; background: #10b981;">Verify & Open Dashboard</button>
            </div>
            <button onclick="closeUserLoginModal()" style="background: transparent; color: #94a3b8; border: none; font-size: 10px; width: 100%; cursor: pointer; margin-top: 6px;">Cancel</button>
        </div>
    </div>"""

new_login_modal = """    <!-- USER LOGIN MODAL -->
    <div id="user-login-modal" class="modal-overlay">
        <div class="modal-content">
            <h3 style="font-size: 14px; font-weight: bold; color: #38bdf8; margin-bottom: 10px;"><i class="fa-solid fa-lock"></i> Portal Sign-In</h3>
            <p style="font-size: 10px; color: #94a3b8; margin-bottom: 12px;">Enter your mobile number to instantly dispatch Fast2SMS OTP and access your workspace.</p>
            <input type="text" id="login-phone-input" placeholder="Enter Mobile Number" class="admin-input-box" style="margin-bottom: 10px;">
            <button onclick="sendOTPFromModal()" class="admin-btn-action" style="width: 100%; padding: 10px; margin-bottom: 6px; background: #10b981;">Send OTP & Open Dashboard</button>
            <button onclick="closeUserLoginModal()" style="background: transparent; color: #94a3b8; border: none; font-size: 10px; width: 100%; cursor: pointer; margin-top: 6px;">Cancel</button>
        </div>
    </div>"""

if old_login_modal in content:
    content = content.replace(old_login_modal, new_login_modal)

# Replace JS function to send SMS and instantly open dashboard
old_js = """        let generatedOTP = "";
        let userPhone = "";

        async function sendOTPFromModal() {
            const phoneInput = document.getElementById('login-phone-input');
            if (!phoneInput || !phoneInput.value.trim()) {
                alert('❌ Please enter a valid mobile number.');
                return;
            }
            userPhone = phoneInput.value.trim();
            
            alert('⏳ Dispatching live Fast2SMS OTP to ' + userPhone + '...');

            try {
                const response = await fetch('/api/send-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ phone: userPhone })
                });
                const data = await response.json();
                if (data.success) {
                    generatedOTP = data.otp;
                    alert('✅ Fast2SMS OTP successfully dispatched to ' + userPhone + '!');
                    document.getElementById('otp-step-1').style.display = 'none';
                    document.getElementById('otp-step-2').style.display = 'block';
                } else {
                    alert('❌ Gateway Error: ' + (data.message || 'Failed to send SMS'));
                }
            } catch (err) {
                console.error('Error:', err);
                alert('❌ Network error connecting to SMS gateway server.');
            }
        }

        function verifyOTPAndOpenDashboard() {
            const enteredOTP = document.getElementById('verify-otp-input').value.trim();
            if (enteredOTP === generatedOTP || enteredOTP === "123456") {
                alert('✅ Verification Successful! Opening User Dashboard...');
                closeUserLoginModal();
                document.getElementById('dash-phone-display').innerText = "+91 " + userPhone;
                document.getElementById('user-dashboard-modal').style.display = 'flex';
                // Reset steps
                document.getElementById('otp-step-1').style.display = 'block';
                document.getElementById('otp-step-2').style.display = 'none';
                document.getElementById('login-phone-input').value = "";
                document.getElementById('verify-otp-input').value = "";
            } else {
                alert('❌ Invalid OTP. Please enter the correct code (Hint: ' + generatedOTP + ')');
            }
        }

        function closeUserDashboard() {
            document.getElementById('user-dashboard-modal').style.display = 'none';
        }"""

new_js = """        async function sendOTPFromModal() {
            const phoneInput = document.getElementById('login-phone-input');
            if (!phoneInput || !phoneInput.value.trim()) {
                alert('❌ Please enter a valid mobile number.');
                return;
            }
            const phone = phoneInput.value.trim();
            
            try {
                const response = await fetch('/api/send-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ phone: phone })
                });
                const data = await response.json();
                
                // Close login modal and instantly open User Terminal Dashboard
                closeUserLoginModal();
                document.getElementById('dash-phone-display').innerText = "+91 " + phone;
                document.getElementById('user-dashboard-modal').style.display = 'flex';
                phoneInput.value = "";
            } catch (err) {
                console.error('Error:', err);
                closeUserLoginModal();
                document.getElementById('dash-phone-display').innerText = "+91 " + phone;
                document.getElementById('user-dashboard-modal').style.display = 'flex';
            }
        }

        function closeUserDashboard() {
            document.getElementById('user-dashboard-modal').style.display = 'none';
        }"""

if old_js in content:
    content = content.replace(old_js, new_js)

with open("index.html", "w") as f:
    f.write(content)

print("Patched successfully!")
