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

  if (request.method === 'Your_Method') {

      // Your code goes here! 😄

    } else if (request.method === 'Your_Method') {

        // Your code goes here! 🤩

   } else {
  	
      // Your error code goes here! 🤕

   }
});

server.listen(3000, () => {
  console.log('Mood feed server running at http://localhost:3000');
});

