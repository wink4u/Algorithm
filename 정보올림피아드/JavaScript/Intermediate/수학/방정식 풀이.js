const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [a, b, c, w] = input[0].split(' ').map(Number)

const dp  = new Array(w + 1).fill(Infinity)
dp[0] = 0

for (let i = 1; i <= w; i++) {
    for (const coin of [a, b, c]) {
        if (coin <= i && dp[i - coin] + 1 < dp[i]) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1)
        }
    }
}

console.log(dp[w])