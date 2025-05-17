const path = require('path');

const fullPath = path.join(
  'Users',
  'nik.piao430',
  'Desktop',
  'my-projects',
  'codedex',
  'node_JS',
  'chaotic',
  'photos'
);

console.log(fullPath);

const files = [
  'boulder.tiff',
  'mountain.png',
  'rocks.jpg',
  'grass.gif',
  'ocean.svg',
  'waves.jpeg'
];

const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff'];

// Find the first image file
const firstImage = files.find(file =>
  imageExtensions.includes(path.extname(file).toLowerCase())
);

if (firstImage) {
  console.log('First image file found:', path.join(fullPath, firstImage));
} else {
  console.log('No image files found!');
}






