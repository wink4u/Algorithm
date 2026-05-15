const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");

const N = Number(input[0])
const M = Number(input[1])

let ans = 1
const DP = Array(N + 1).fill(0)
for (let i = 0; i < M; i++){
    DP[Number(input[2 + i])] = -1
}

let flag = 0
for (let i = 1; i <= N; i++){
    if (DP[i] === -1) {
        if (DP[i - 1] === 0 || DP[i - 1] === -1) continue
        ans *= DP[i - 1]
        flag = 0
        continue
    }

    if (!flag) {
        DP[i] = 1
        flag =1 
    } else if (flag === 1) {
        DP[i] = 2
        flag = 2
    } else {
        DP[i] = DP[i - 1] + DP[i - 2]
    }
}

ans *= (DP[N] === -1 ? 1 : DP[N])
console.log(ans)