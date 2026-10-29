with open("index.html", "r") as f:
    html = f.read()

# Direct client-side Fast2SMS implementation script
direct_script = """
<script>
async function requestOtp(event) {
    if (event) event.preventDefault();
    const phoneInput = document.querySelector('input[type="tel"]') || document.querySelector('input[placeholder*="8122252222"]') || document.getElementById('mobile-input');
    const mobile = phoneInput ? phoneInput.value : '8122252222';

    if (!mobile || mobile.length < 10) {
        alert('Please enter a valid 10-digit mobile number');
        return;
    }

    const apiKey = '0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK';
    const otp = Math.floor(1000 + Math.random() * 9000).toString();

    try {
        const response = await fetch('https://www.fast2sms.com/dev/bulkV2', {
            method: 'POST',
            headers: {
                'authorization': apiKey,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                route: 'otp',
                variables_values: otp,
                numbers: mobile
            })
        });

        const data = await response.json();
        if (data.return) {
            alert('OTP successfully sent via Fast2SMS to ' + mobile);
        } else {
            alert('Fast2SMS Error: ' + (data.message || JSON.stringify(data)));
        }
    } catch (err) {
        alert('Request failed: ' + err.message);
    }
}
</script>
"""

# Append the script before closing body tag
if "requestOtp" not in html:
    html = html.replace("</body>", direct_script + "\n</body>")

with open("index.html", "w") as f:
    f.write(html)
with open("public/index.html", "w") as f:
    f.write(html)
