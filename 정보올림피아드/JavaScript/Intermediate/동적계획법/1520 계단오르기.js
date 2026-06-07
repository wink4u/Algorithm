const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = [0].concat(input.slice(1).map(Number))
const DP = Array(N + 1).fill(0)

if (N <= 2) {
    console.log(arr.slice(0, N + 1).reduce((a, b) => a + b, 0))
} else {
    DP[1] = arr[1]
    DP[2] = arr[1] + arr[2]

    for (let i = 3; i <= N; i++){
        DP[i] = arr[i] + Math.max(DP[i - 3] + arr[i - 1], DP[i - 2])
    }
    console.log(DP[N])
}
