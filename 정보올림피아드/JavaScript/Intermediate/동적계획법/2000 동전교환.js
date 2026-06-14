const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)
const w = Number(input[2])

const DP = Array(w + 1).fill(Infinity)

for (let i = 0; i < N; i++){
    DP[arr[i]] = 1
}
for (let i = 1; i <= w; i++){
    for (let j = 0; j < N; j++){
        if (i - arr[j] >= 1) {
            DP[i] = Math.min(DP[i], DP[i - arr[j]] + 1)
        }
    }
}

console.log(DP[w])