const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const s = input[1].trim()
const DP = Array.from(Array(N), () => Array(3).fill(0))
let ans = 0

for (let i = 0; i < N; i++){
    if (i !== 0){
        for (let j = 0; j < 3; j++){
            DP[i][j] = DP[i - 1][j]
        }
    }

    if (s[i] === 'D'){
        if (i === 0) DP[i][0] = 1
        else DP[i][0] = DP[i - 1][0] + 1
    } else if (s[i] === 'K'){
        if (i !== 0) DP[i][1] = DP[i - 1][0] + DP[i - 1][1]
    } else if (s[i] === 'S') {
        if (i !== 0) DP[i][2] = DP[i - 1][1] + DP[i - 1][2]
    } else if (s[i] === 'H'){
        if (i !== 0) ans += DP[i - 1][2]
    }
}

console.log(ans)