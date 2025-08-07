"""
-- OLD:
Instructions
Create a good-morning.js program that prints a message if it's early in the day.

Define an hour variable and give it the current time of day.

Write an if statement for the following:

If hour < 12, print “Good morning 🌞” and some of your morning routines.
After you run the code, change hour's value and run it again. Do this a few times to make sure the program is working as intended.



-- NEW:

Go back to your if statement from the previous exercise and turn it into an if/else for the following:

If hour < 12, then print “Good morning 🌞” and some of your morning routines.
Else, print “Good afternoon ☁️” and some of your afternoon rituals.
After you run the code, change hour's value and run it again. Do this a few times to make sure the program is working as intended.

"""

// Old 

let hour = 2;

if (hour < 12) {
  console.log('Good Morning 🌞');
} 



// NEW

let hour = 12;

if (hour < 12) {
  console.log('Good morning 🌞')
} else {
  console.log('Good afternoon ☁️')
}
