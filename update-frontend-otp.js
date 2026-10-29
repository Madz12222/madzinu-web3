import fs from 'fs';

const htmlPath = 'public/index.html';
if (!fs.existsSync(htmlPath)) {
    console.error('❌ public/index.html not found!');
    process.exit(1);
}

let html = fs.readFileSync(htmlPath, 'utf8');

// Replace simulated OTP alert with real backend fetch call
const oldOtpFunctionPattern = /function\s+sendOtp\s*\(\)\s*\{[\s\S]*?\}/;
const newOtpFunction = `
async function sendOtp() {
    const phoneInput = document.getElementById('phoneInput') || document.querySelector('input[type="tel"]');
    const phone = phoneInput ? phoneInput.value : prompt('Enter mobile number for OTP:');
    
    if (!phone || phone.length < 10) {
        alert('Please enter a valid mobile number.');
        return;
    }

    try {
        const res = await fetch('/api/send-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone })
        });
        const data = await res.json();
        if (data.success) {
            alert('🚀 Real OTP Dispatched via Fast2SMS Gateway successfully!');
        } else {
            alert('❌ Failed to send OTP: ' + (data.message || 'Unknown error'));
        }
    } catch (err) {
        console.error('Error:', err);
        alert('❌ Network error connecting to SMS gateway.');
    }
}
`;

if (oldOtpFunctionPattern.test(html)) {
    html = html.replace(oldOtpFunctionPattern, newOtpFunction);
} else {
    // Inject before body close if function name differs
    html = html.replace('</body>', `<script>${newOtpFunction}</script></body>`);
}

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('✅ Frontend OTP handler updated successfully in public/index.html!');
