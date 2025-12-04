const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [a, k] = input[0].split(' ').map(Number)
const DP = Array(k + 1).fill(Infinity)


DP[a] = 0

for (let i = a; i < k; i++){
    const idx = i
    DP[idx + 1] = Math.min(DP[idx + 1], DP[idx] + 1)

    const double = idx * 2

    if (double <= k){
        DP[double] = Math.min(DP[idx] + 1, DP[double])
    }
}

console.log(DP[k])