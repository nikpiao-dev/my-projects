// Checkpoint Javascript Project - Horoscope

// define variables:

const birthMonth = Math.floor(Math.random() * 12) + 1; // generate random month
let zodiac = "";

let fortune = '';
let randomFortune = Math.floor(Math.random() * 7); // i will do only 6 random fortunes (Fortune Cookie Generator)


// Even fortunes (randomFortune 2, 4, 6)
if (randomFortune % 2 === 0) { 
    if (randomFortune === 2) {
        fortune = 'A smile is your passport into the hearts of others.';
    } else if (randomFortune === 4) {
        fortune = 'Hard work pays off in the future, laziness pays off now. Never give up. You\'re not a failure if you don\'t give up. The love of your life is stepping into your planet this summer.';
    } else if (randomFortune === 6) {
        fortune = 'You will be showered with unexpected kindness in the near future.';
    }
} 
// Odd fortunes (randomFortune 1, 3, 5)
else {
    if (randomFortune === 1) {
        fortune = 'You will be hungry again in one hour.';
    } else if (randomFortune === 3) {
        fortune = 'It\'s better to be alone sometimes.';
    } else if (randomFortune === 5) {
        fortune = 'A new opportunity will appear when you least expect it.';
    }
}

// horoscope conditional statements:
if (birthMonth === 1) {
    zodiac = "♑ Capricorn - January: Your ambition might make it hard to tolerate anything less than perfection.";
} else if (birthMonth === 2) {
    zodiac = "♒ Aquarius - February: Focus on home and family brings comfort and meaningful moments this week.";
} else if (birthMonth === 3) {
    zodiac = "♓ Pisces - March: Explore your local community—you might make surprising connections and create a unique, memorable celebration.";
} else if (birthMonth === 4) {
    zodiac = "♈ Aries - April: With Mercury in Taurus, it's time to get practical and focus on boosting your finances, while keeping Mother’s Day low-key but thoughtful.";
} else if (birthMonth === 5) {
    zodiac = "♉ Taurus - May: With the stars aligning for introspection and creativity, use this time to wrap up loose ends and enjoy a laid-back Mother’s Day in your own style.";
} else if (birthMonth === 6) {
    zodiac = "♊ Gemini - June: This weekend, focus on tying up loose ends and embracing the moment—Mother’s Day is all about enjoying the simple joys with those closest to you.";
} else if (birthMonth === 7) {
    zodiac = "♋ Cancer - July: Step outside your comfort zone and embrace new connections, while Mother’s Day invites you to celebrate with style, making the day as lively and special as possible.";
} else if (birthMonth === 8) {
    zodiac = "♌ Leo - August: Focus on your career goals and take the opportunity to connect with influential people, while Mother’s Day calls for a heartfelt and nurturing celebration filled with love.";
} else if (birthMonth === 9) {
    zodiac = "♍ Virgo - September: Embrace a broader perspective this weekend with exciting explorations, while Mother’s Day invites you to enjoy a casual, adventurous celebration full of fun discoveries.";
} else if (birthMonth === 10) {
    zodiac = "♎ Libra - October: Focus on reading between the lines and tuning into body language this weekend, while Mother’s Day encourages intimate, meaningful connections with those who matter most.";
} else if (birthMonth === 11) {
    zodiac = "♏ Scorpio - November: Strengthen your connections with personal, in-person interactions this weekend, while Mother’s Day invites you to plan a celebration that’s thoughtful and all about nurturing yourself and those you love.";
} else if (birthMonth === 12) {
    zodiac = "♐ Sagittarius - December: Get organized and prioritize your tasks this weekend, while Mother’s Day encourages a calm and thoughtful celebration that lets you unwind and appreciate the moms around you.";
} else {
    zodiac = "Unknown Zodiac!";
}


console.log('Birth Month:', birthMonth);
console.log();

console.log("Horoscope: ", zodiac);
console.log();

console.log("Fortune: " + fortune);
console.log();
