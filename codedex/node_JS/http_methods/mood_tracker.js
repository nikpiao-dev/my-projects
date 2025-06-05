// Instructions
// It's time to tie all the HTTP methods you learned together in a virtual mood ring! 💍

// Imagine you’re building a mood tracker app. It's like a twitter feed, but with tiny updates about your mood. 🥰

// Combine any two of the methods we learned in this chapter to manage a single mood variable. Here's what your server should do:

// GET: Show the current mood
// POST: Add a new mood
// PATCH: Edit the mood
// PUT: Replace the mood entirely
// DELETE: Remove the mood post
// If you want a bonus challenge, try combining all five HTTP Methods in this exercise.

// Here's some code to get you started!

const http = require('http');

let mood = '';

const server = http.createServer((request, response) => {

  if (request.method === 'POST') {
    request.on('data', (tweet) => {
      mood += tweet;
    });
    request.on('end', () => {
      console.log('New mood:', mood)

    // Send a simple response
    response.writeHead(200, { 'Content-Type': 'text/plain' });
    response.end('Tweet received!');
    });
  } else if (request.method === 'PATCH') {

  if (request.method === 'PATCH') {
    let addition = '';

    request.on('data', (tweet) => {
      addition += tweet;
    });

    request.on('end', () => {
      console.log('Original mood:', mood);
      mood = ' ' + addition; // Append new content to the end
      console.log('New mood:', mood)
       
      response.writeHead(200, { 'Content-Type': 'text/plain' });
      response.end('Mood patched!');
    });
  }
  } else {
    response.writeHead(404, { 'Content-Type': 'text/plain' });
    response.end('Go back to your terminal!');
  }
});


server.listen(3000, () => {
  console.log('Mood feed server running at http://localhost:3000');
});

// cURL command:
// curl -X PATCH http://localhost:3000 -d 'I love Node.js!'
// curl -X POST http://localhost:3000 -d 'I love Javascript!'
