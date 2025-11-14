const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const num = input[1].split(' ').map(Number)
const DP = Array.from(Array(N - 1), () => Array(21).fill(0n))

DP[0][num[0]] = 1n

for (let i = 1; i < N - 1; i++){
    for (let j = 0; j <= 20; j++){
        if (j + num[i] <= 20) DP[i][j + num[i]] += DP[i - 1][j]
        if (j - num[i] >= 0) DP[i][j - num[i]] += DP[i - 1][j]
    }
}

console.log(DP[N - 2][num[N - 1]].toString())