import fs from 'fs';

const htmlPath = 'public/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

const debugScript = `
<script>
async function sendOtp() {
    const phoneInput = document.getElementById('phoneInput');
    const phone = phoneInput ? phoneInput.value : '';
    
    if (!phone || phone.length < 10) {
        alert('Please enter a valid 10-digit mobile number.');
        return;
    }

    alert('Sending request to backend for ' + phone + '...');

    try {
        const res = await window.fetch('/api/send-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone })
        });
        
        const data = await res.json();
        console.log('Server response:', data);
        
        if (data.success) {
            alert('🚀 Real OTP Sent via Fast2SMS successfully!');
        } else {
            alert('❌ Failed: ' + (data.message || JSON.stringify(data)));
        }
    } catch (err) {
        console.error('Fetch error:', err);
        alert('❌ Network Error: ' + err.message);
    }
}
</script>
`;

if (html.includes('async function sendOtp')) {
    html = html.replace(/async function sendOtp\(\)\s*\{[\s\S]*?\}/, debugScript);
} else {
    html = html.replace('</body>', debugScript + '</body>');
}

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('✅ Added debug alerts to sendOtp function!');
