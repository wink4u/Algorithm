const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)

const DP = Array(N).fill(1)

for (let i = 1; i < N; i++){
    for (let j = i - 1; j >= 0; j--){
        if (arr[i] > arr[j]) {
            DP[i] += DP[j]
            DP[i] %= 998244353
        }

    }
}

console.log(DP.join(' '))