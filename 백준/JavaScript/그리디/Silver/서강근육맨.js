const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(BigInt)
arr.sort((a, b) => (a < b ? - 1 : a > b ? 1 : 0))
let min = null

if (N === 1) {
    console.log(arr[0].toString())
    process.exit()
}

if (N % 2) {
    min = arr.pop()
}

let left = 0, right = arr.length - 1

while (left < right) {
    const sum = arr[left] + arr[right]

    if (min === null || sum > min) {
        min = sum
    }
    left++
    right--
}

console.log(min.toString())