const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const num = String(input[0]).split('').map(v => Number(v))
const DP = Array.from(Array(num.length), () => Array(35).fill(0))
DP[0][num[0]] = 1

for (let i = 1; i < num.length; i++){
    for (let j = 1; j < 35; j++){
        const nxt = 10 * j + num[i]

        if (nxt <= 34) {
            DP[i][nxt] += DP[i - 1][j]
        }

        DP[i][num[i]] += DP[i - 1][j]
    }
}

console.log(DP[num.length - 1].slice(1).reduce((a, b) => a + b, 0))