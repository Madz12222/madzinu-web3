import fs from 'fs';

const htmlPath = 'public/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');

// If there are multiple script tags or functions, let's remove any string matching "Gateway! [Code:"
if (html.includes('Gateway! [Code:')) {
    console.log('🔍 Found old simulated OTP code in HTML. Cleaning it up...');
    html = html.replace(/OTP Dispatched via Fast2SMS Gateway!/g, 'Backend Dispatched via API!');
}

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('✅ Cleaned HTML file!');
