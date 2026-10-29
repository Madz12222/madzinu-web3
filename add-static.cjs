const fs = require('fs');
let serverCode = fs.readFileSync('server.js', 'utf8');

const staticMiddleware = `
import path from 'path';
import { fileURLToPath } from 'url';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
app.use(express.static(path.join(__dirname, 'public')));
`;

const fallbackRoute = `
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
`;

if (!serverCode.includes('express.static')) {
    // Insert static middleware after app initialization
    serverCode = serverCode.replace(/const app = express\(\);/, `const app = express();\n${staticMiddleware}`);
    // Insert fallback route near the bottom before export or listen
    serverCode = serverCode.replace(/export default app;/, `${fallbackRoute}\nexport default app;`);
    
    fs.writeFileSync('server.js', serverCode, 'utf8');
    console.log('STATIC SERVING ADDED SUCCESSFULLY');
} else {
    console.log('Static serving already present.');
}
