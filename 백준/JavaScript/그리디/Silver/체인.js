const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)

if (N <= 2) {
    console.log(1)
} else {
    arr.sort((a, b) => a - b)

    let total = N
    let cnt = 1

    for (let i = 0; i < N; i++){
        if (cnt + arr[i] >= total) break

        cnt += arr[i]
        total--
    }

    console.log(cnt - 1)
}