const fs = require('fs');

fs.readFile('today.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file', err);
        return;
    }
    console.log(data);
});