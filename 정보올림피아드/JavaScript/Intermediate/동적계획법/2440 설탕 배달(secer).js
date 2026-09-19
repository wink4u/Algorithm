const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])

if (N <= 2) {
    console.log(-1)
} else {
    const DP = Array(N + 1).fill(Infinity)

    if (N >= 3) DP[3] = 1
    if (N >= 5) DP[5] = 1

    for (let i = 6; i <= N; i++){
        DP[i] = Math.min(DP[i - 3] + 1, DP[i - 5] + 1)
    }

    console.log(DP[N] === Infinity ? - 1: DP[N])
}