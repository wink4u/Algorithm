const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))


arr.sort((a, b) => {
    if (a[0] < b[0]) return -1
    else if (a[0] === b[0]) {
        if (a[1] < b[1]) return -1
    }

    return 1
})

let ans = 0
let before = arr[0][1]


for (let i = 1; i < N; i++){
    const [left, right] = arr[i]

    if (before < left) {
        ans++
        before = right
    } else {
        before = before < right ? before : right
    }

}

console.log(ans + 1)