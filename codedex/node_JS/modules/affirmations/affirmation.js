const fs = require('fs');
const path = require('path');
const os = require('os');

const affirmations = [
  'This is gonna be your year!',
  'You can absolutely climb that V4!',
  'Every day, in every way, you’re getting better and better.',
  'You are stronger than any challenge that comes your way.',
  'Success is in your future—keep pushing forward.',
  'Your hard work is paying off.',
  'Believe in yourself and all that you are.',
  'You have the power to create change.',
  'Stay positive, work hard, and make it happen.',
  'You are worthy of all the good things life has to offer.'
];

const desktopPath = path.join(os.homedir(), 'Desktop');

function saveRandomAffirmationToDesktop() {
  const randomAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
  const newFilePath = path.join(desktopPath, 'daily-affirmations.txt');

  fs.writeFile(newFilePath, randomAffirmation, (err) => {
    if (err) {
      console.error('Error writing the affirmation to the file:', err);
    } else {
      console.log('Random affirmation saved to:', newFilePath);
    }
  });
}

saveRandomAffirmationToDesktop();

