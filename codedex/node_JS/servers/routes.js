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
    
    } else if (req.url === '/living-room') {
        content = '<h1>Living Room</h1><p>A cozy space with a plush sofa, a roaring fireplace, and a place to relax with family and friends.</p>';
    
    } else if (req.url === '/dining-room') {
        content = '<h1>Dining Room</h1><p>A beautiful setting for shared meals, laughter, and the clinking of glasses over hearty conversations.</p>';
    
    } else if (req.url === '/kitchen') {
        content = '<h1>Kitchen</h1><p>The heart of the home, filled with delicious aromas and bustling with the joy of creating meals.</p>';
    
    } else if (req.url === '/bedroom') {
        content = '<h1>Bedroom</h1><p>A tranquil retreat designed for restful nights and dreamy mornings bathed in sunlight.</p>';
    
    } else if (req.url === '/office') {
        content = '<h1>Office</h1><p>A quiet corner dedicated to productivity, creativity, and a touch of inspiration.</p>';
    
    } else if (req.url === '/bathroom') {
        content = '<h1>Bathroom</h1><p>A spa-like oasis where you can unwind and rejuvenate your mind and body.</p>';
    
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
