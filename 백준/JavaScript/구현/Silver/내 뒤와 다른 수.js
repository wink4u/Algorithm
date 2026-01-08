const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(BigInt)

const ans = []
let cnt = 1
for (let i = 1; i < N; i++){
    if (arr[i] === arr[i - 1]) cnt++
    else {
        ans.push(`${i + 1}`.repeat(cnt))
        cnt = 1
    }
}

const reAns = ans.join('').split('')

for (let i = 0; i < cnt; i++){
    reAns.push(-1)
}

console.log(reAns.join(' '))
