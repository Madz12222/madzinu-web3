import fs from 'fs';

const htmlPath = 'public/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

// Force overwrite any sendOtp function with a clean direct fetch call
const directFetchScript = `
<script>
async function sendOtp() {
    const phone = document.getElementById('phoneInput').value;
    if (!phone || phone.length < 10) {
        alert('Please enter a valid 10-digit mobile number.');
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
            alert('🚀 Live SMS Dispatched via Fast2SMS to ' + phone);
        } else {
            alert('❌ Gateway Error: ' + (data.message || 'Failed'));
        }
    } catch (err) {
        alert('❌ Network connection error.');
    }
}
</script>
`;

// Append or replace before body close
if (html.includes('async function sendOtp')) {
    // Replace old async function
    html = html.replace(/async function sendOtp\(\)\s*\{[\s\S]*?\}/, directFetchScript);
} else {
    html = html.replace('</body>', directFetchScript + '</body>');
}

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('✅ Forced direct backend fetch into sendOtp function!');
