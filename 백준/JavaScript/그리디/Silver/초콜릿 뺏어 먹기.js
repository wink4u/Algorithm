const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

const min = arr[0]
let day = 0, cnt = 0

for (let i = 1; i < N; i++){
    if (arr[i] > min) {
        day++
        cnt += (arr[i] - min)
    }
}

console.log(cnt, day)
