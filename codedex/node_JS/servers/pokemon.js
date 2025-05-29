// Pokemon Center
// codedex - NodeJS


// import http module
const http = require('http');


// create a Pokemon Center Server

const server = http.createServer((req, res) => {

    // Default response settings
    let statusCode = 200;
    let contentType = 'text/html; charset=utf-8';
    let content = '';

    if (req.url === '') {
        content = '<h1>Pokémon Center</h1><br><p>A special place where Pokémon find care, healing, and trainers get a fresh start for their journey.</p>';
    } else if (req.url === 'pikachu') {}
    else if (req.url === 'sylveon') {}
    else if (req.url === '') {}
    else if (req.url === '') {}
    else if (req.url === '') {}

    else {
        // If the route doesn't match, send a 404 error
        statusCode = 404;
        content = '<h1>404 Not Found</h1><p>Page does not exist.</p>';
    } 
    res.writeHead(statusCode, {'Content-Type': contentType})
    res.end(content);

});

server.listen(3000, () => {
    console.log('Pokemon Center starts at http://localhost:3000/');
});

