with open("index.html", "r") as f:
    content = f.read()

old_otp_func = """        let generatedOTP = "";
        let userPhone = "";

        async function sendOTPFromModal() {
            const phoneInput = document.getElementById('login-phone-input');
            if (!phoneInput || !phoneInput.value.trim()) {
                alert('❌ Please enter a valid mobile number.');
                return;
            }
            userPhone = phoneInput.value.trim();
            generatedOTP = Math.floor(100000 + Math.random() * 900000).toString();
            
            alert('🚀 Fast2SMS OTP: ' + generatedOTP + ' (Dispatched to ' + userPhone + ')');
            
            // Switch to OTP verification step inside modal
            document.getElementById('otp-step-1').style.display = 'none';
            document.getElementById('otp-step-2').style.display = 'block';
        }"""

new_otp_func = """        let generatedOTP = "";
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
        }"""

if old_otp_func in content:
    content = content.replace(old_otp_func, new_otp_func)
    with open("index.html", "w") as f:
        f.write(content)
    print("Updated frontend OTP function successfully!")
else:
    print("Could not match exact frontend OTP function.")
