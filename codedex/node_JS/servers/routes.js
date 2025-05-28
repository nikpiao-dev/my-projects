// Dream House
// codedex


// import 'http' module
const http = require('http');


// create a server

const server = http.server((res, req) => {
    // Default response settings
    let statusCode = 200;
    let contentType = 'text/html; charset=utf-8';
    let content = '';

    // Content based on the requested route
    if (req.url === '/') {
        content = '<h1>Dream House</h1><p>A special place where your dreams find a home and every moment feels like a fresh start.</p>';
    
    } else if (req.url === '') {

    } else if (req.url === '') {

    } else if (req.url === '') {

    } else if (req.url === '') {

    } else if (req.url === '') {

    } else if (req.url === '') {

    } else {
        // If the route doesn't match, send a 404 error
        statusCode = 404;
        content = '<h1>404 Not Found</h1><p>Page does not exist.</p>';
    }


    // final response
    res.writeHead(statusCode, {'Content-Type': contentType});
    res.end(content);
});





server.listen(3000, () => {
    console.log('Visit dream house at http://localhost:3000/');
});
