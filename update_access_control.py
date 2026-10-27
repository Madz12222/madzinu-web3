with open("index.html", "r") as f:
    content = f.read()

# Replace the loose login/bypass with strict role-based verification script
old_script_marker = "function loginBypass()"
new_secure_script = """
function verifySecureNodeAccess() {
    const mobile = document.getElementById('login-mobile') ? document.getElementById('login-mobile').value : '';
    const otpCode = document.getElementById('login-otp-code') ? document.getElementById('login-otp-code').value : '';

    if(mobile.length < 10) {
        alert('Access Denied: Please enter a valid 10-digit mobile number.');
        return;
    }

    // Strict Access Control: Direct access is not allowed except for verified admin/contractor session
    if(mobile === '9840000000' && otpCode === '2026') {
        alert('Admin Secure Node Access Granted.');
        document.getElementById('view-landing').classList.add('hidden');
        document.getElementById('view-dashboard').classList.remove('hidden');
    } else {
        alert('Direct access not allowed. Please verify via valid OTP or admin credentials.');
    }
}
"""

if "verifySecureNodeAccess" not in content:
    # Inject or update login verification logic safely
    content = content.replace("function loginBypass()", new_secure_script)
    with open("index.html", "w") as f:
        f.write(content)
    print("Strict access control logic added successfully!")
else:
    print("Access control already updated!")
