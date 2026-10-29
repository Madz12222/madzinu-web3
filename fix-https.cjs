const fs = require('fs');
let code = fs.readFileSync('server.js', 'utf8');

if (!code.includes("import https from 'https'") && !code.includes('import https from "https"')) {
    code = "import https from 'https';\n" + code;
    fs.writeFileSync('server.js', code, 'utf8');
    console.log('ADDED HTTPS IMPORT SUCCESSFULLY');
} else {
    console.log('HTTPS import already exists.');
}
