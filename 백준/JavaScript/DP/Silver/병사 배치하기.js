const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)

const DP = Array(N).fill(1)

for (let i = 1; i < N; i++){
    for (let j = 0; j < i; j++){
        if (arr[i] < arr[j]) {
            DP[i] = Math.max(DP[i], DP[j] + 1)
        }
    }
}

console.log(N - Math.max(...DP))