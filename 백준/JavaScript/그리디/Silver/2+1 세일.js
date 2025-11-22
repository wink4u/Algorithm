const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map((v) => Number(v))

let ans = 0
arr.sort((a, b) => a - b)

let q = []

while (arr.length) {
    q.push(arr.pop())

    if (q.length === 3) {
        ans += (q[0] + q[1])
        q = []
    }
}

if (q.length) {
    for (let i = 0; i < q.length; i++){
        ans += q[i]
    }
}

console.log(ans.toString())