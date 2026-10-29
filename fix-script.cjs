const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// If the file ends with raw JS code without a script tag, let's wrap it properly
// Let's check if there is an unwrapped try { block at the end
const lastScriptClose = html.lastIndexOf('</script>');
const lastTry = html.lastIndexOf('try {');

if (lastTry > lastScriptClose) {
    // Insert <script> right before the last try block and </script> at the end
    html = html.substring(0, lastTry) + '<script>\ntry {' + html.substring(lastTry + 5) + '\n</script>';
    fs.writeFileSync('index.html', html);
    console.log('Successfully wrapped trailing JavaScript block in <script> tags!');
} else {
    console.log('Script tags are already properly balanced.');
}
