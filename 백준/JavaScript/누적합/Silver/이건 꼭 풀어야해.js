const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, Q] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

const sum = [0]
arr.sort((a, b) => a - b)

for (let i = 0; i < N; i++) {
    sum.push(sum[i] + arr[i])
}

const ans = []

for (let i = 0; i < Q; i++) {
    const [L, R] = input[i + 2].split(' ').map(Number)
    ans.push(sum[R] - sum[L - 1])
}

console.log(ans.join('\n'))