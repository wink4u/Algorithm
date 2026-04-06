const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0]);
const board = input.slice(1).map(line =>
    line.trim().split("").map(ch => ch === "T" ? 1 : 0)
);

let answer = Infinity;

for (let mask = 0; mask < (1 << N); mask++) {
    let total = 0;

    for (let col = 0; col < N; col++) {
        let tailCount = 0;

        for (let row = 0; row < N; row++) {
            const flipped = (mask & (1 << row)) ? 1 : 0;
            tailCount += board[row][col] ^ flipped;
        }

        total += Math.min(tailCount, N - tailCount);
    }

    answer = Math.min(answer, total);
}

console.log(answer);