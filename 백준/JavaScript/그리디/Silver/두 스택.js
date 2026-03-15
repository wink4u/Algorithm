const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K] = input[0].split(' ').map(Number)
const A = input[1].split(' ').map(Number)
const B = input[2].split(' ').map(Number)

let aSum = A.reduce((a, b) => a + b, 0)
let bSum = B.reduce((a, b) => a + b, 0)

let cnt = 0

while (cnt < K) {
    if (A.length && B.length) {
        if (aSum < bSum) {
            bSum -= B.pop()
        } else {
            aSum -= A.pop()
        }
    } else if (A.length) {
        aSum -= A.pop()
    } else if (B.length) {
        bSum -= B.pop()
    } else {
        break
    }

    cnt++
}

console.log(bSum >= aSum ? bSum : aSum)