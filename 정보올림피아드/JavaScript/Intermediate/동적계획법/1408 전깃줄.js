const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => v.trim().split(' ').map(Number))

arr.sort((a, b) => {
    if (a[0] > b[0]) return 1
    else return -1
})

const DP = Array(N).fill(1)


for (let i = 1; i < N; i++){
    for (let j = 0; j < i; j++){
        if (arr[j][1] < arr[i][1]) {
            DP[i] = Math.max(DP[i], DP[j] + 1)
        }
    }
}

console.log(N - Math.max(...DP))