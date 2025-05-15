const fs = require('fs');


const message = '☀️✨ Good vibes only! Let\'s make today amazing. 🌈🌸 Rise and shine! Adventure awaits. 🚀💫 Stay positive and sparkle on! ✨🌼';

fs.writeFile('tomorrow.txt', message, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log('File written successfully!');
  }
});

