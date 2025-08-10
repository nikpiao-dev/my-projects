"""

Instructions


Rock Paper Scissors is a classic game that resonates with folks from around the world. The rules are as follows:

Rock beats Scissors.
Scissors beat Paper.
Paper beats Rock.
Let's use conditionals, the random number generator, and create a program that simulates the game between the player and the computer!

Begin with a player variable and give it a 0 to represent "Rock", a 1 to represent "Paper", or a 2 to represent "Scissors."

Then use Math.random() to generate a number between 0 and 2 for another computer variable.

Then, use conditionals to compare the values of player and computer to see who wins!

Player picked:      Rock
Computer picked:    Scissors

The player won!

"""



const player = 2;
const computer = Math.floor(Math.random() * 3);

if (player === 0) {
  if (computer === 0) {
    console.log("Draw");
  } else if (computer === 1) {
    console.log("The computer won!");
  } else if (computer === 2) {
    console.log("The player won!");
  } else {
    console.log("An error occurred");
  }
} else if (player === 1) {
  if (computer === 0) {
    console.log("The player won!");
  } else if (computer === 1) {
    console.log("Draw");
  } else if (computer === 2) {
    console.log("The computer won!");
  } else {
    console.log("An error occurred");
  }
} else if (player === 2) {
  if (computer === 0) {
    console.log("The computer won!");
  } else if (computer === 1) {
    console.log("The player won!");
  } else if (computer === 2) {
    console.log("Draw");
  } else {
    console.log("An error occurred");
  }
} else {
  console.log("An error occurred");
}
