// Create our own new server

const http = require('http');

const server = http.createServer((request, response) => {
    console.log(`Received request: ${request.method} ${request.url}`);
    
    response.writeHead(200, {'Content-Type': 'text/plain; charset=utf-8'});
    response.end('🛒🎥🍽🛍🛋🎞');
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
