const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number)
const list = M === 0 ? [] : input[1].split(' ').map(Number)

const DP = Array.from(Array(N + 6), () => Array(45).fill(Infinity))
DP[0][0] = 0

const check = new Map()

for (const v of list) {
    check.set(v, true)
}


for (let i = 0; i <= N; i++){
    for (let j = 0; j < 40; j++){
        if (DP[i][j] === Infinity) continue

        const v = DP[i][j]
        
        if (check.get(i + 1)) {
            DP[i + 1][j] = Math.min(DP[i + 1][j], v)
        } else {
            if (j >= 3) {
                DP[i + 1][j - 3] = Math.min(DP[i + 1][j - 3], v)
            }
        }

        DP[i + 1][j] = Math.min(DP[i + 1][j], v + 10000)
        
        for (let k = 1; k <= 3; k++){
            DP[i + k][j + 1] = Math.min(DP[i + k][j + 1], v + 25000)
        }

        for (let k = 1; k<= 5; k++){
            DP[i + k][j + 2] = Math.min(DP[i + k][j + 2], v + 37000)
        }
    }
}

console.log(Math.min(...DP[N]))