const os = require('os');

const uptimeInSeconds = os.uptime()


// 7 days in seconds 
const SECONDS_IN_A_WEEK = 60 * 60 * 24 * 7;


// Convert uptime to hours, minutes, and seconds
const hours = Math.floor(uptimeInSeconds / 3600);
const minutes = Math.floor((uptimeInSeconds % 3600) / 60);
const seconds = Math.floor(uptimeInSeconds % 60);


// How long was the machine has been awake?:

const uptimeMessage = `Hiiiii! I've been awake for ${hours} hours, ${minutes} minutes, and ${seconds} seconds.`;

console.log(uptimeMessage);



// Wisdom Message

if (uptimeInSeconds > SECONDS_IN_A_WEEK) {
  console.log('Yikes! I\'ve been running nonstop for over a week... I need a break, please! 😴🛌 Time for some serious Zzzs!');
} else {
  console.log('All systems go! 🚀 Less than a week awake and still feeling fresh, sharp, and ready to crush it! 💪✨');
}

