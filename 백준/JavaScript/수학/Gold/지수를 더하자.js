const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const prime = input[1].split(' ').map(Number)
const K = Number(input[2])
let ans = 0

for (let i = 0; i < N; i++){
    let cnt = 0
    let num = K

    while (num > 1) {
        const v = Math.floor(num / prime[i])
        cnt += v
        num = v
    }

    ans += cnt
}

console.log(ans)