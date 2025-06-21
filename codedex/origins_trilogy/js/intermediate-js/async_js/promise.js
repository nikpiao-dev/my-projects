"""

Instructions
Let's get started with making promises. 🤝

In the random-numbers.js file, define a randomNumberPromise() function that returns a new Promise object. This object should include a callback function that either resolves or rejects the promise.

Inside the callback function, create a random number between 1 and 10.

If the number is less than 5, use resolve().
Otherwise, use reject().

"""

// Define randomNumberPromise() function here 💖

const generateBtn = document.getElementById("generateButton");

generateBtn.addEventListener("click", randomNumberPromise);

