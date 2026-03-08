const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))
let ans = 0
const check = Array(1000001).fill(0)

for (const [a, b, c] of arr) {
    if (!check[a] && !check[b] && !check[c]) {
        ans++
    }
    check[a] = 1
    check[b] = 1
    check[c] = 1 
}

console.log(ans)