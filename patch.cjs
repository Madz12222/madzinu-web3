const fs = require('fs');
let html = fs.readFileSync('public/index.html', 'utf8');

// Replace the mock alert with the real API fetch
const oldSnippet = "const generatedOTP = Math.floor(100000 + Math.random() * 900000);\n        alert('Backend Dispatched via API! [Code: ' + generatedOTP + ']');";

const newSnippet = `fetch('/api/send-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone: document.querySelector('input').value })
        })
        .then(res => res.json())
        .then(data => alert('SMS Gateway Response: ' + JSON.stringify(data)))
        .catch(err => alert('Error: ' + err.message));`;

if (html.includes(oldSnippet)) {
    html = html.replace(oldSnippet, newSnippet);
    fs.writeFileSync('public/index.html', html, 'utf8');
    console.log('PATCHED SUCCESSFULLY');
} else {
    // Fallback: replace any alert containing 'Backend Dispatched via API'
    html = html.replace(/alert\('Backend Dispatched via API!.*?'\);/g, `
        fetch('/api/send-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone: document.querySelector('input').value })
        })
        .then(res => res.json())
        .then(data => alert('SMS Gateway Response: ' + JSON.stringify(data)))
        .catch(err => alert('Error: ' + err.message));
    `);
    fs.writeFileSync('public/index.html', html, 'utf8');
    console.log('PATCHED VIA FALLBACK REGEX');
}
