const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])

const DP = Array.from({ length: N + 1} , (_, i) => i)

for (let i = 1; i < N - 2; i++){
    for (let j = i + 3; j < N + 1; j++){
        DP[j] = Math.max(DP[j], DP[i] * (j - i - 1))
    }
}

console.log(DP[N])