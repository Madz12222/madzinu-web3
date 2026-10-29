const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Find the exact spot where the raw code starts at the bottom and insert <script>
const target = "try { const res = await fetch('/api/send-otp'";
const idx = html.indexOf(target);

if (idx !== -1) {
    // Insert <script>\n right before the try block
    html = html.substring(0, idx) + '<script>\n' + html.substring(idx);
    
    // Ensure there is a closing </script> right before </body>
    // First, let's remove any duplicate closing script tags if present, then add a clean one
    html = html.replace(/<\/script>/g, ''); 
    // Add single valid closing script tag right before </body>
    html = html.replace('</body>', '</script>\n</body>');
    
    fs.writeFileSync('index.html', html);
    console.log('Successfully wrapped bottom JS in <script> tags!');
} else {
    console.log('Target string not found.');
}
