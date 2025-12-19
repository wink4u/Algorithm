const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const weapon = input.slice(1).map((v) => v.split(' ').map(Number))

const DP = Array.from(Array(N), () => Array(M).fill(0))

for (let i = 0; i < M; i++){
    DP[0][i] = weapon[0][i]
}

for (let i = 1; i < N; i++){
    for (let j = 0; j < M; j++){
        let min = Infinity

        for (let k = 0; k < M; k++){
            if (j !== k) {
                if (min > DP[i - 1][k]) min = DP[i - 1][k]
            }
        }

        DP[i][j] = weapon[i][j] + min
    }
}

console.log(Math.min(...DP[N - 1]))