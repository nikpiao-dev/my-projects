const jokeContainer = document.getElementById("jokeContainer");
const getJokeBtn = document.getElementById("getJokeBtn");

function fetchJoke() {
  // Fetch for joke data and use chaining here 💖

  fetch('https://official-joke-api.appspot.com/random_joke')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);

    console.log(`Joke: ${data.setup}`);
    console.log(`Punchline: ${data.punchline}`);
    console.log(`Type: ${data.type}`);
    console.log(`ID: ${data.id}`);


    const joke = `<p>${data.setup}</p><p>${data.punchline}</p>`;
    jokeContainer.innerHTML = joke;
  })
  .catch((error) => console.error('Error fetching joke:', error));
  jokeContainer.innerHTML = '<p>Sorry, unable to fetch joke. Please try again later.</p>';
}

getJokeBtn.addEventListener("click", fetchJoke);
