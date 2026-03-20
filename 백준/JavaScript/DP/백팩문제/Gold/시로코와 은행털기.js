const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [n, k, x] = input[0].split(" ").map(Number);
const arr = [];

for (let i = 1; i <= n; i++) {
    const [a, b] = input[i].split(" ").map(Number);
    arr.push(a);
}

const maxSum = k * x;
const dp = Array.from({ length: k + 1 }, () => Array(maxSum + 1).fill(false));
dp[0][0] = true;

for (const a of arr) {
    for (let cnt = k - 1; cnt >= 0; cnt--) {
        for (let sum = maxSum - a; sum >= 0; sum--) {
            if (dp[cnt][sum]) {
                dp[cnt + 1][sum + a] = true;
            }
        }
    }
}

let ans = 0;
for (let sumA = 0; sumA <= maxSum; sumA++) {
    if (dp[k][sumA]) {
        const sumB = k * x - sumA;
        ans = Math.max(ans, sumA * sumB);
    }
}

console.log(ans.toString());