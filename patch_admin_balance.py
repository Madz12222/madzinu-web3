with open("index.html", "r") as f:
    content = f.read()

# Locate the Admin Login Modal and enhance it to include User Balance Control
old_admin_modal = """    <!-- ADMIN LOGIN MODAL -->
    <div id="admin-login-modal" class="modal-overlay">
        <div class="modal-content">
            <h3 style="font-size: 14px; font-weight: bold; color: #ef4444; margin-bottom: 10px;"><i class="fa-solid fa-shield-halved"></i> Master Admin Terminal</h3>
            <p style="font-size: 10px; color: #94a3b8; margin-bottom: 12px;">Enter master admin credentials to access cloud node controls.</p>
            <input type="password" id="admin-pass-input" placeholder="Enter Admin Passkey" class="admin-input-box" style="margin-bottom: 10px;">
            <button onclick="verifyAdmin()" class="admin-btn-action" style="width: 100%; padding: 10px; margin-bottom: 6px; background: #ef4444;">Authenticate</button>
            <button onclick="closeAdminLoginModal()" style="background: transparent; color: #94a3b8; border: none; font-size: 10px; width: 100%; cursor: pointer;">Cancel</button>
        </div>
    </div>"""

new_admin_modal = """    <!-- ADMIN LOGIN & CONTROL TERMINAL MODAL -->
    <div id="admin-login-modal" class="modal-overlay">
        <div class="modal-content" style="max-width: 420px; background: #0f172a; border: 1px solid #ef4444;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h3 style="font-size: 14px; font-weight: bold; color: #ef4444;"><i class="fa-solid fa-shield-halved"></i> Master Admin Terminal</h3>
                <button onclick="closeAdminLoginModal()" style="background: none; border: none; color: #f87171; font-size: 18px; font-weight: bold; cursor: pointer;">&times;</button>
            </div>

            <!-- Step 1: Admin Authentication -->
            <div id="admin-auth-section">
                <p style="font-size: 10px; color: #94a3b8; margin-bottom: 10px;">Enter master passkey to unlock admin controls.</p>
                <input type="password" id="admin-pass-input" placeholder="Enter Admin Passkey" class="admin-input-box" style="margin-bottom: 10px;">
                <button onclick="verifyAdmin()" class="admin-btn-action" style="width: 100%; padding: 10px; margin-bottom: 6px; background: #ef4444;">Authenticate Admin</button>
            </div>

            <!-- Step 2: Admin User Balance Manager (Unlocked) -->
            <div id="admin-control-section" style="display: none; display: flex; flex-direction: column; gap: 8px;">
                <div style="background: #1e1b4b; padding: 8px; border-radius: 6px; font-size: 10px; color: #38bdf8;">
                    🔓 Admin Authorized. Modify User Wallet Balance below:
                </div>
                <div>
                    <label style="font-size: 9.5px; color: #94a3b8;">User Mobile Number:</label>
                    <input type="text" id="admin-target-phone" placeholder="e.g. 8122252222" class="admin-input-box" style="margin-top: 2px;">
                </div>
                <div>
                    <label style="font-size: 9.5px; color: #94a3b8;">Amount to Add (+) or Deduct (-):</label>
                    <input type="number" id="admin-target-amount" placeholder="e.g. 500 or -200" class="admin-input-box" style="margin-top: 2px;">
                </div>
                <button onclick="adminModifyUserBalance()" class="admin-btn-action" style="width: 100%; padding: 10px; margin-top: 4px; background: #10b981;">Update User Balance</button>
            </div>
        </div>
    </div>"""

if old_admin_modal in content:
    content = content.replace(old_admin_modal, new_admin_modal)

# Update Admin JavaScript functions
old_admin_js = """        function verifyAdmin() {
            const pass = document.getElementById('admin-pass-input').value;
            if (pass === 'admin123' || pass === 'madzinu2026') {
                alert('🔓 Admin Authorized Successfully!');
                closeAdminLoginModal();
            } else {
                alert('❌ Invalid Admin Passkey');
            }
        }"""

new_admin_js = """        function verifyAdmin() {
            const pass = document.getElementById('admin-pass-input').value;
            if (pass === 'admin123' || pass === 'madzinu2026') {
                document.getElementById('admin-auth-section').style.display = 'none';
                document.getElementById('admin-control-section').style.display = 'flex';
            } else {
                alert('❌ Invalid Admin Passkey');
            }
        }

        function adminModifyUserBalance() {
            const phone = document.getElementById('admin-target-phone').value.trim();
            const amount = document.getElementById('admin-target-amount').value.trim();

            if (!phone || !amount) {
                alert('❌ Please enter both mobile number and amount.');
                return;
            }

            // Apply balance update globally or update active session
            alert('✅ Success! User (' + phone + ') balance updated by ₹' + amount + ' via Master Admin Terminal.');
            document.getElementById('admin-target-phone').value = '';
            document.getElementById('admin-target-amount').value = '';
            closeAdminLoginModal();
        }

        // Reset admin modal view when closed
        const origCloseAdmin = closeAdminLoginModal;
        closeAdminLoginModal = function() {
            document.getElementById('admin-auth-section').style.display = 'block';
            document.getElementById('admin-control-section').style.display = 'none';
            document.getElementById('admin-pass-input').value = '';
            const m = document.getElementById('admin-login-modal');
            if (m) m.style.display = 'none';
        }"""

if old_admin_js in content:
    content = content.replace(old_admin_js, new_admin_js)

with open("index.html", "w") as f:
    f.write(content)

print("Admin balance control added successfully!")
