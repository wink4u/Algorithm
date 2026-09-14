const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)
arr.sort((a, b) => a - b)

let ans = 3000000001
let l = 0, m = 0, r = 0
const check = (left) => {
    let mid = left + 1, right = N - 1

    while (mid < right) {
        const v = arr[left] + arr[mid] + arr[right]
    
        if (Math.abs(v) < ans) {
            ans = Math.abs(v)
            l = arr[left], m = arr[mid], r= arr[right]
        }
    
        if (v >= 0) {
            right--
        } else {
            mid++
        }
    }
}

for (let i = 0; i < N - 2; i++) {
    check(i)
}

console.log(l, m, r)