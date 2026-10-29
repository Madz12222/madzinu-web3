const fs = require('fs');
let code = fs.readFileSync('server.js', 'utf8');

// Update the Fast2SMS API URL construction to use route=q instead of route=otp
code = code.replace(
    /route=otp/g,
    'route=q'
);

// Also ensure authorization parameter is correctly formatted
code = code.replace(
    /authorization=([^&]+)/g,
    'authorization=0aN18piLoRT2xYt7QhgbyIPEmUucVO4qf9GSkFjHzWXM5Z6sed4GTFX7lmwJeRuqPSO5IhB06MLWgzHK'
);

fs.writeFileSync('server.js', code, 'utf8');
console.log('ENDPOINT UPDATED TO ROUTE=Q WITH HARDCODED KEY');
