const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)
arr.sort((a, b) => a - b)
const K = 0

let left = 0, right = N - 1
let ans = 1000000001
let l = arr[left], r = arr[right]

while (left < right) {
    const v = arr[left] + arr[right]

    if (Math.abs(v) < ans) {
        ans = Math.abs(v)
        l = arr[left], r= arr[right]
    }

    if (v >= 0) {
        right--
    } else {
        left++
    }
}

console.log(l, r)