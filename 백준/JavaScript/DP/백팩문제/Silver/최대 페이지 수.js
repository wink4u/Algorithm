const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const DP = Array(N + 1).fill(0)
const page = input.slice(1).map((v) => v.split(' ').map(Number))

for (let i = 0; i < M; i++){
    const [day, v] = page[i]
    for (let j = N; j >= day; j--){
        DP[j] = Math.max(DP[j - day] + v, DP[j])
    }
}

console.log(DP[N])
