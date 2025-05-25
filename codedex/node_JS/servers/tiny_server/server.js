// Emoji Story - Servers section
// Codedex - Node.js course

const http = require('http');  // Import the http module

// Create a server
const server = http.createServer((request, response) => {
    console.log(`Received request: ${request.method} ${request.url}`);

    response.writeHead(200, {'Content-Type': 'text/plain; charset=utf-8'});
    response.end('🛒🎥🍽🛍🛋🎞');
});


// Start the server and listen on port 3000
server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
