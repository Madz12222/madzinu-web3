const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Find where the duplicate stray fetch/try block starts at the bottom and cut it off completely
const targetIndex = html.indexOf("try { const res = await fetch('/api/send-otp'");
if (targetIndex !== -1) {
    // Keep everything BEFORE the duplicate snippet, and cleanly append closing tags
    // Let's find the last proper closing script tag before this duplicate block
    const cleanHtml = html.substring(0, targetIndex).trim() + '\n</div>\n</body>\n</html>';
    fs.writeFileSync('index.html', cleanHtml);
    console.log('Successfully removed duplicate trailing code block!');
} else {
    console.log('Target string not found.');
}
