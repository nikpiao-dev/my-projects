"""

Instructions
Let's practice these nifty new operators by planning an intercontinental vacation! 🗺️

Define a planVacation() function that returns a string array of destinations we plan to visit. It should accept at least two string arguments:
destinationOne
destinationTwo
Use the rest operator so the planVacation() function can have more arguments passed to it.

Then, execute the planVacation() function and log the results to the console.


"""


const planVacation = (destinationOne, destinationTwo, ...moreDestination) => {
  return [destinationOne, destinationTwo, ...moreDestination];
};

console.log(planVacation('Brazil', 'Spain', 'Taiwan', 'Dubai', 'Cape Town'));
