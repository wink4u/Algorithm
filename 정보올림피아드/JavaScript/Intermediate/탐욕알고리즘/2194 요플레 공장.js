const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split("\n");

const [N, S] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.split(' ').map(Number))

let prev = arr[0][0]
let ans = prev * arr[0][1]

for (let i = 1; i < N; i++){
    const now = arr[i][0]

    prev = Math.min(prev + S, now)
    ans += prev * arr[i][1]
}

console.log(ans)