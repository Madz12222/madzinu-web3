const fs = require('fs');
let code = fs.readFileSync('server.js', 'utf8');

// Replace the Fast2SMS route url to use bulkV2 with route=q
code = code.replace(
    /\/dev\/bulkV2\?authorization=/,
    '/dev/bulkV2?route=q&'
);

// If it's using the old otp route, replace it completely
code = code.replace(
    /route=otp/,
    'route=q'
);

fs.writeFileSync('server.js', code, 'utf8');
console.log('UPDATED TO BULKV2 ROUTE');
