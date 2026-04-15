const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [D, N] = input[0].split(' ').map(Number)
const day = input.slice(1, D + 1).map(Number)
const arr = input.slice(D + 1).map(v => v.split(' ').map(Number))

const check = Array.from(Array(D), () => Array(N).fill(0))
const DP = Array.from(Array(D), () => Array(N).fill(0))

for (let i = 0; i < D; i++){
    for (let j = 0; j < N; j++){
        const [A, B, C] = arr[j]

        if (A <= day[i] && day[i] <= B) check[i][j] = 1
    }
}

for (let i = 1; i < D; i++){
    for (let j = 0; j < N; j++){
        if (check[i][j]) {
            for (let k = 0; k < N; k++){
                if (check[i - 1][k]) {
                    DP[i][j] = Math.max(DP[i][j], DP[i - 1][k] + Math.abs(arr[j][2] - arr[k][2]))
                }
            }
        }
    }
}

console.log(Math.max(...DP[D - 1]))