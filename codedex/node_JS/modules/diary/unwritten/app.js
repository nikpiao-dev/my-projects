const fs = require('fs');

const filePath = "seventh-grade.txt";

fs.unlink(filePath, (err) => {
  if (err) {
    console.error('Error deleting file:', err);
    return;
 }
    console.log('seventh-grade.txt has been deleted.');
});
