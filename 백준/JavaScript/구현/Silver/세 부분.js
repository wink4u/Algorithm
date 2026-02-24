const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const str = input[0];
const N = str.length;

let answer = null;

for (let i = 1; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {

        const part1 = str.slice(0, i).split("").reverse().join("");
        const part2 = str.slice(i, j).split("").reverse().join("");
        const part3 = str.slice(j).split("").reverse().join("");

        const check = part1 + part2 + part3;

        if (answer === null || check < answer) {
            answer = check;
        }
    }
}

console.log(answer);