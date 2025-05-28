const http = require('http');

// Create a server object

const server = http.createServer((request, response) => {
  response.write('Hello, World!');
  response.end();
});


//server.listen(3000);

server.listen(3000, function () {
  console.log('Server running at http://localhost:3000');
});

// Go to http://localhost:3000

// Ctrl + C to exit server
