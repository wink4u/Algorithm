const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)

arr.sort((a, b) => a - b)
const K = N % 2 ? Math.floor(N / 2) + 1 : Math.floor(N / 2)
const checkArr = []

for (let i = 0; i < K; i++){
    checkArr.push(arr[i])
}

let cnt = 0


const cal = (num) => {
    let tmp = 0
    while (num > 1) {
        num = Math.floor(num / 2)
        tmp++
    }

    return tmp
}

for (let i = 0; i < K; i++){
    cnt += cal(checkArr[i])
}

console.log(cnt + 1)