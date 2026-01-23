const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)

if (N === 1) console.log(0)
else {
    let left = 0, right = 1
    let ans = 0

    while (left < right && right < N) {
        if (arr[left] < arr[right]) {
            ans = Math.max(ans, arr[right] - arr[left])
            right++
        } else {
            left = right
            right = left + 1
        }
    }

    console.log(ans)
}