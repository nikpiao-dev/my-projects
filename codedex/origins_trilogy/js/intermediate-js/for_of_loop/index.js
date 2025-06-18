"""

On Spotify, the top 5 most streamed songs have over 18 billion listens combined! 🤯

The most-streamed-songs.js file is importing a array of objects about each of these five songs.

On line 29, let's use for...of and for...in loops to display info about these songs on the console.

The output should look like this:

Blinding Lights
The Weeknd
4260000000

Shape of You
Ed Sheeran
3901000000

Someone You Loved
Lewis Capaldi
3413000000

Sunflower
Post Malone (feat. Swae Lee)
3345000000

As It Was
Harry Styles
3278000000

"""

const fiveMostStreamedSongs = [
  {
    title: "Blinding Lights",
    artist: "The Weeknd",
    streams: 4260000000,
  },
  {
    title: "Shape of You",
    artist: "Ed Sheeran",
    streams: 3901000000,
  },
  {
    title: "Someone You Loved",
    artist: "Lewis Capaldi",
    streams: 3413000000,
  },
  {
    title: "Sunflower",
    artist: "Post Malone (feat. Swae Lee)",
    streams: 3345000000,
  },
  {
    title: "As It Was",
    artist: "Harry Styles",
    streams: 3278000000,
  },
];

// Iterate through each song here 💖

for (let streamedSong of fiveMostStreamedSongs) {
  // console.log(streamedSong);
  for (let info in streamedSong) {
    console.log(streamedSong[info]);
  }
  console.log();
}
