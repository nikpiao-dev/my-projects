// Cyber Ramen Shop
// Codedex


// import 'http' module
const http = require('http');


// Create a server 
const server = http.createServer((response, request) => {
    console.log(`Received request: ${request.method} ${request.url}`);
    response.writeHead(200, {'Content-Type': 'text/plain; charset=utf-8'});

     // menu creation using response.write()
    response.write('Welcome to Neon Noodles!\n\n\n');
    response.write('==============');
    response.write('LATE NITE MENU');
    response.write('==============\n');
    response.write('Ramen');
    response.write('1. Quantum Truffle Ramen')
    response.write('2. Spicy Ramen');
    response.write('3. Midnight Dumplings');
    response.write('4. Glow-in-the-Dark Sushi');
    response.write('5. Quantum Bao Buns \n');
    response.write('EXTRA TOPPINGS');
    response.write('1. Hacktivist Pork');
    response.write('2. Cybernetic Egg');
    response.write('3. Glowing Scallions');

    response.write('\nEnjoy your meal!\n');
    
});


// Start server and listen on port 3000
server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});