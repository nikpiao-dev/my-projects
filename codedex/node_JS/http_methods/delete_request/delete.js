// Use what we learned above to create a status message 
// and then delete it using the DELETE request.

const http = require('http');

let message = "Currently decoding alien signals. Might be late for lunch 🛸📡";

const server = http.createServer((req, res) => {
    if (req.method === 'DELETE') {
        console.log('Original Message:', message);
        message = null;
        console.log('Message deleted.')

        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Message deleted!');
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Go back to your terminal!');
    }
});

server.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});