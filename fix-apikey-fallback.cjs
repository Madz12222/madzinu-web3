const fs = require('fs');
let code = fs.readFileSync('server.js', 'utf8');

// Replace process.env.FAST2SMS_API_KEY with fallback to your actual key string if env is missing
const targetKey = '0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK';

code = code.replace(
    /process\.env\.FAST2SMS_API_KEY/g,
    `(process.env.FAST2SMS_API_KEY || '${targetKey}')`
);

fs.writeFileSync('server.js', code, 'utf8');
console.log('API KEY FALLBACK APPLIED SUCCESSFULLY');
