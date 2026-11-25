const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0]);
const arr = [0].concat(input[1].split(' ').map(Number))


const sumArr = new Array(N + 1).fill(0);
const check = new Map()

for (let i = 1; i <= N; i++){
    sumArr[i] = sumArr[i - 1] + arr[i]

    const v = check.get(arr[i])
    if (v) {
        check.get(arr[i]).push(i);
    } else {
        check.set(arr[i], [i])
    }
}

let maxValue = 0
let cnt = 0


const checkValue = (value) => {
    if (maxValue < value) {
        maxValue = value
        cnt = 1
    } else if (maxValue === value) {
        cnt++
    }
}

check.forEach((value, key) => {
    const l = value.length
    
    const v = l > 1 ? sumArr[value[l - 1]] - sumArr[value[0] - 1] : sumArr[value[0]] - sumArr[value[0] - 1]
    checkValue(v)
})

console.log(maxValue, cnt)
