const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, T] = input[0].split(' ').map(Number)
let idx = 1;

const v = Array(1001).fill(0)

let max = 0
let min = 1001

for (let n = 0; n < N; n++){
    const K = Number(input[idx++])

    for (let k = 0; k < K; k++){
        const [s, e] = input[idx++].split(' ').map(Number)
        min = Math.min(min, s)
        max = Math.max(max, e)

        for (let i = s + 1; i <= e; i++){
            v[i]++
        }
    }
}


for (let i = 1; i <= max; i++){
    v[i] += v[i - 1]
}

let ans = 0
let start = 0, end = 0

for (let i = min + T; i <= max; i++){
    const total = v[i] - v[i - T]

    if (total > ans) {
        ans = total
        start = i - T, end = i
    }
}

console.log(start, end)