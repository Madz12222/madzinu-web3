const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Look for where the trailing code/fetch starts near the bottom
const targetStr = "try { const res = await fetch('/api/send-otp'";
const idx = html.indexOf(targetStr);

if (idx !== -1) {
    // Insert <script> right before the try block, and ensure it closes before </body>
    let updated = html.substring(0, idx) + '<script>\n' + html.substring(idx);
    // Add closing </script> right before </body>
    updated = updated.replace(/\n<\/body>/, '\n</script>\n</body>');
    fs.writeFileSync('index.html', updated);
    console.log('Successfully wrapped bottom script inside <script> tags!');
} else {
    console.log('Target string not found.');
}
