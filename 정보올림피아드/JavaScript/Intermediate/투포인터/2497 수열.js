const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, K] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

let ans = arr.slice(0, K).reduce((a, b) => a + b, 0)
let tmp = ans

let left = 0, right = K

while (right < N) {
    tmp -= arr[left++]
    tmp += arr[right++]

    ans = Math.max(ans, tmp)
}

console.log(ans)