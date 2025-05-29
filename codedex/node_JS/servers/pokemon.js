// Pokemon Center
// codedex - NodeJS


// import http module
const http = require('http');


// create a Pokemon Center Server

const server = http.createServer((req, res) => {

    // Default response settings
    let statusCode = 200;
    let textType = 'text/html; charset=utf-8';
    let contentType = 'text/html'
    let content = '';

    if (req.url === '') {
        content = '<h1>Pokémon Center</h1><br><p>A special place where Pokémon find care, healing, and trainers get a fresh start for their journey.</p>';
    } else if (req.url === '/pikachu') {
        console.log("Pika Pika!");
        content = `
            <h1>Pikachu's Room</h1>
            <img src="https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png" alt="Pikachu" style="width:300px;">
            <p>Pikachu is feeling energetic!</p>
        `;
    } else if (req.url === '/sylveon') {
        console.log("Sylv Sylv!");
        content = `
            <h1>Sylveon's Room</h1>
            <img src="https://assets.pokemon.com/assets/cms2/img/pokedex/full/700.png" alt="Sylveon" style="width:300px;">
            <p>Sylveon is relaxing gracefully.</p>
        `;
    } else {
        // If the route doesn't match, send a 404 error
        statusCode = 404;
        content = `
            <h1>404 Not Found</h1>
            <p>This Pokémon is currently resting!</p>
        `;
    } 

    // Set the header and status code
    res.writeHead(statusCode, { 'Content-Type': contentType });

    res.write(content)
    res.end('Gotta code ’em all! 🐦‍🔥');

});

server.listen(3000, () => {
    console.log('Visit Pokemon Center at http://localhost:3000/');
});

