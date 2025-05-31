// Visitor Counter App for Get Requests:

const http = require('http');

// Variable goes here 😊
let count = 0; 

const server = http.createServer((request, response) => {
  // Your code also goes here 🤗
  if (request.method === 'GET') {
    count++;
    console.log(`Visitor Count: ${count}`)
  }
  
});

server.listen(3000, () => {
  console.log('Visitor Counter running at http://localhost:3000');
});
