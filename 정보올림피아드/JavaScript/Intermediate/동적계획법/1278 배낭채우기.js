const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [N, W] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.split(' ').map(Number))

const DP = Array(W + 1).fill(0)
for (let i = 0; i < N; i++){
    const [w, v] = arr[i]

    for (let j = W; j >= w; j--){
        DP[j] = Math.max(DP[j], DP[j - w] + v)
    }
}

console.log(DP[W])