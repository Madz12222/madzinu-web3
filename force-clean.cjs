const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

// Find the copyright line and truncate everything after its closing container
const marker = 'Secure Cloud Node.';
const pos = content.indexOf(marker);

if (pos !== -1) {
    const cutOffPoint = pos + marker.length;
    // Keep everything up to the marker, then close the tags properly
    let clean = content.substring(0, cutOffPoint);
    // Find the next closing div, body, html tags if any exist nearby, or append them
    clean += '\n</div>\n</body>\n</html>';
    fs.writeFileSync('index.html', clean);
    console.log('Successfully purged trailing code from index.html!');
} else {
    console.log('Marker not found.');
}
