// GET Counter 📈
// Codédex

const http = require('http'); // Import the http module

let visitorCount = 0;

const server = http.createServer((request, response) => {
  if (request.method === 'GET') {
    visitorCount++;
    console.log(`Visitor Count: ${visitorCount}`);
    // No response sent to browser
  }
});

server.listen(3000, () => {
  console.log('Visitor Counter running at http://localhost:3000');
});