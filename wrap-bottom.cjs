const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Find the stray un-tagged fetch/try code at the bottom and wrap it
if (!html.includes('<script>') || html.lastIndexOf('try {') > html.lastIndexOf('</script>')) {
    // Replace the last occurrence of try { with <script>\ntry {
    const lastTry = html.lastIndexOf('try {');
    if (lastTry !== -1) {
        html = html.substring(0, lastTry) + '<script>\ntry {' + html.substring(lastTry + 5);
        // Ensure there's a closing </script> right before </body>
        html = html.replace(/\n<\/body>/, '\n</script>\n</body>');
        fs.writeFileSync('index.html', html);
        console.log('Successfully wrapped bottom script!');
    }
}
