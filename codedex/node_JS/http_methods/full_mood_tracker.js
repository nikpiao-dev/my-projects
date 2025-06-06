const http = require('http');

let mood = '';

const server = http.createServer((request, response) => {
  if (request.method === 'GET') {
    response.writeHead(200, { 'Content-Type': 'text/plain' });
    response.end(`Current mood: ${mood || 'No mood set yet.'}`);

  } else if (request.method === 'POST') {
    let body = '';
    request.on('data', chunk => body += chunk);
    request.on('end', () => {
      mood += body;
      console.log('Mood added:', mood);
      response.writeHead(200, { 'Content-Type': 'text/plain' });
      response.end('Mood added!');
    });

  } else if (request.method === 'PATCH') {
    let patchData = '';
    request.on('data', chunk => patchData += chunk);
    request.on('end', () => {
      console.log('Original mood:', mood);
      mood += ' ' + patchData;
      console.log('Patched mood:', mood);
      response.writeHead(200, { 'Content-Type': 'text/plain' });
      response.end('Mood patched!');
    });

  } else if (request.method === 'PUT') {
    let newMood = '';
    request.on('data', chunk => newMood += chunk);
    request.on('end', () => {
      mood = newMood;
      console.log('Mood replaced:', mood);
      response.writeHead(200, { 'Content-Type': 'text/plain' });
      response.end('Mood replaced!');
    });

  } else if (request.method === 'DELETE') {
    mood = '';
    console.log('Mood deleted.');
    response.writeHead(200, { 'Content-Type': 'text/plain' });
    response.end('Mood deleted!');
    
  } else {
    response.writeHead(405, { 'Content-Type': 'text/plain' });
    response.end('Method not allowed');
  }
});

server.listen(3000, () => {
  console.log('Mood feed server running at http://localhost:3000');
});

// # POST: Add to current mood
// curl -X POST http://localhost:3000 -d 'Feeling happy.'

// # GET: View current mood
// curl http://localhost:3000

// # PATCH: Modify/append to current mood
// curl -X PATCH http://localhost:3000 -d ' And excited for the day!'

// # PUT: Replace the entire mood
// curl -X PUT http://localhost:3000 -d 'Feeling calm and centered.'

// # DELETE: Clear mood
// curl -X DELETE http://localhost:3000
