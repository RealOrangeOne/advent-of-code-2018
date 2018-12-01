const fs = require('fs');

const frequencies = fs.readFileSync('data.txt').toString().split("\n").map((element) => parseInt(element)).filter((element) => !isNaN(element));

console.log(frequencies.reduce((a, b) => a + b, 0));

let currentFrequency = 0;
let seenFrequencies = new Set([currentFrequency]);
let count  = 0;
while (true) {
    frequencies.forEach((frequency) => {
        currentFrequency += frequency;
        if (seenFrequencies.has(currentFrequency)) {
            console.log(currentFrequency);
            process.exit(0);
        }
        seenFrequencies = seenFrequencies.add(currentFrequency);
    });
    count += 1;
    console.log(count, currentFrequency);
}
