"""
Instructions
Using JSX attributes, let's build an image gallery!

Above the return statement in the App.js, paste the following:

const barcelonaImage = <img src={{/* code here */}}  alt="Barcelona" />;
const tokyoImage = <img src={{/* code here */}}  alt="Tokyo" />;
const ohioImage = <img src={{/* code here */}}  alt="Ohio" />;

Then, add the following strings to the src attribute for each <img> variable:

barcelonaImage --> "https://i.imgur.com/qaQNzqi.png"
tokyoImage --> "https://i.imgur.com/OAx1wzO.png"
ohioImage --> "https://i.imgur.com/CxJjltu.png"
Next, create an imageGallery array of the three variables you just made.

Make each item a <li> list item element that contains one of these variables.

Lastly, add the imageGallery array to the <ul> element in the return statement.
"""


export default function App() {
  const barcelonaImage = <img src={"https://i.imgur.com/qaQNzqi.png"}  alt="Barcelona" />;
  const tokyoImage = <img src={"https://i.imgur.com/OAx1wzO.png"}  alt="Tokyo" />;
  const ohioImage = <img src={"https://i.imgur.com/CxJjltu.png"}  alt="Ohio" />;

  const imageGallery = [
    <li>{barcelonaImage}</li>,
    <li>{tokyoImage}</li>,
    <li>{ohioImage}</li>
  ]

  return (
    <ul>
      {imageGallery}
    </ul>
  );
}
