"""
Instructions:

Goodreads is a popular resource for keeping track of the books you read. Let's imitate this with ES6! 📖

Define a goodreadsInfo object with the following structure:

const goodreadsInfo = {
  currentlyReading: [
    {
      title: "",
      author: ""
    }
  ],

  wantToRead: [
    {
      title: "",
      author: ""
    }
  ]
}

Add at least one book object (with a title and author) to each array.

## addNewBooks() Function
This part tests our knowledge of the spread and rest operators.

Define an addNewBooks() arrow function with the following parameters:

A books array of strings.
An optional additionalBookObjects array.
This function should return a new array that includes all items from books along with any items from the additionalBookObjects array.

Then, use this function on at least one of the lists from the goodreadsInfo object, like so:

goodreadsInfo.currentlyReading = addNewBooks(goodreadsInfo.currentlyReading, /* new books here */);

## showGoodreadsInfo() Function
This part tests our knowledge of loops and template literals.

Define a showGoodreadsInfo() function that accepts a single info parameter.

Inside, create two variables representing the reading list arrays from the info parameter.

Then, use a combination of console.log() statements, for...of loops, and template literals to output our reading lists to the console.

Lastly, execute the showGoodreadsInfo() function. The output should look similar to this:

Currently Reading:
The Hobbit by J.R.R. Tolkien
The Two Towers by J.R.R. Tolkien
The MOM Test by Rob Fitzpatrick

Want to Read:
The Art of Language Invention by David Peterson
Looking for Alaska by John Green


"""


// Define object here 💖

const goodreadsInfo = {
  currentlyReading: [
    {
      title: "Digital Shadows: The Firewall Protocol",
      author:  "Aria Kastrel",
      genre: "Cyberpunk Thriller / Techno-thriller"
    }
  ],

  wantToRead: [
    {
      title: "The Cipher Garden",
      author: "Elion Varic",
      genre: "Mystery / Sci-Fi"
    },
    {
      title: "Static Whispers: Tales from the Signal Void",
      author: "Mina Cross",
      genre: "Sci-Fi Horror / Anthology"
    }
  ]
}

// Define addBooks() function here 💖

const addNewBooks = (books, additionalBookObjects = []) => {
  return [...books, ...additionalBookObjects];
};

goodreadsInfo.currentlyReading = addNewBooks(goodreadsInfo.currentlyReading, [
  {
    title: "Neon Helix",
    author: "Jax Riven",
    genre: "Cyberpunk / Biopunk"
  }
]);

goodreadsInfo.wantToRead = addNewBooks(goodreadsInfo.wantToRead, [
  {
    title: "Silicon Requim",
    author: "Nova Rennes",
    genre: "Dystopian Tech Noir"
  }
]);


// console.log(goodreadsInfo.currentlyReading);
// console.log(goodreadsInfo.wantToRead);
// console.log();

// Define showGoodreadsInfo() function here 💖

const showGoodreadsInfo = (info) => {
  const currentlyReading = info.currentlyReading;
  const wantToRead = info.wantToRead;

  console.log("Currently Reading:")
  for (let book of currentlyReading) {
    console.log(`${book.title} by ${book.author} - ${book.genre}`);
  }
  console.log();

  console.log("Want to Read:");
  for (let book of wantToRead) {
    console.log(`${book.title} by ${book.author} - ${book.genre}`)
  }
  console.log();
}

showGoodreadsInfo(goodreadsInfo);
