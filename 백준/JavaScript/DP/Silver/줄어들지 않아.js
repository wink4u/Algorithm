const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0])

const DP = Array.from(Array(65), () => Array(11).fill(0))

for (let i = 0; i < 10; i++){
    DP[1][i] = 1
}

DP[1][10] = 10

for (let i = 2; i < 65; i++){
    let tmp = 0
    for (let j = 0; j < 10; j++) {

        for (let k = j; k < 10; k++){
            DP[i][j] += DP[i - 1][k]
        }
        tmp += DP[i][j]
    }
    DP[i][10] = tmp
}

for (let i = 1; i <= T; i++){
    const n = Number(input[i])
    console.log(DP[n][10])
}