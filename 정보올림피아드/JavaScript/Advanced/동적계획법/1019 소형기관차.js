const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const n = Number(input[0])
const arr = input[1].split(' ').map(Number)
const k = Number(input[2])

const s = [0]

let tmp = 0
for (let i = 0; i < n; i++){
    tmp += arr[i]
    s.push(tmp)
}

const DP = Array.from(Array(4), () => Array(n + 1).fill(0))

for (let i = 1; i < 4; i++){
    for (let j = i * k; j < n + 1; j++){

        if (i === 1) {
            DP[i][j] = Math.max(DP[i][j - 1], s[j] - s[j - k])
        } else {
            DP[i][j] = Math.max(DP[i][j - 1], DP[i - 1][j - k] + s[j] - s[j - k])
        }
    }
}

console.log(DP[3][n])