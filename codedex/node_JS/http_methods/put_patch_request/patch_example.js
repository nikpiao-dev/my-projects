Let's revisit the username example, but with PATCH instead of PUT.

const http = require('http');

let username = '@rihanna';

const server = http.createServer((request, response) => {
  if (request.method === 'PATCH') {
    let patchData = '';

    request.on('data', (chunk) => {
      patchData += chunk;
    });

    request.on('end', () => {
      console.log('Original Username:', username);

      // Only update the username with the patch data (assuming it's a string to append)
      username += patchData;
      
      console.log('Updated Username:', username);

      response.writeHead(200, { 'Content-Type': 'text/plain' });
      response.end('Username patched!');
    });
  } else {
    response.writeHead(404, { 'Content-Type': 'text/plain' });
    response.end('Go back to your terminal!');
  }
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});


Here's the cURL command:

curl -X PATCH http://localhost:3000 -d "1234"

And here's what we'd see in the console:

Original Username: @rihanna
Updated Username: @badgalriri
