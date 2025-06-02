// Use patch to modify a short bio

const http = require('http');
const { console } = require('inspector');

let post = '📍 Lost in a world of good vibes';

const server = http.createServer((request, response) => {
    if (request.method === 'PATCH') {
        let patchData = '';

        request.on('data', (tweet) => {
            patchData += tweet;
        });

        request.on('end', () => {
            console.log('Original bio:', post)

            // Only update the post with patch data (assume a string)
            post += patchData;

            console.log('Updated bio:', post)

            request.writeHead(200, { 'Content-Type': 'text/plain' });
            request.readableEnded('New bio patched!');
        });
    } else {
        response.writeHead(400, { 'Content-Type': 'text/plain'});
        response.end('Go back to your terminal!')
    }
});


server.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});