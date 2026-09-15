const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

const sum = new Array(N + 1).fill(0)

for (let i = 1; i <= N; i++) {
    sum[i] = sum[i - 1] + arr[i - 1]
}

let ans = 0

for (let i = M; i <= N; i++){
    ans = Math.max(ans, sum[i] - sum[i - M])
}

console.log(ans)
