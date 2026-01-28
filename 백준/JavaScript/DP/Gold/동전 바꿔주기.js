const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const T = Number(input[0])
const k = Number(input[1])
const DP = Array(T + 1).fill(0)
DP[0] = 1

for (let i = 0; i < k; i++){
    const [coin, cnt] = input[i + 2].split(' ').map(Number)
    for (let j = T; j > 0; j--){
        for (let c = 1; c <= cnt; c++){
            const check = j - (coin * c)
            if (check >= 0) DP[j] += DP[check]

        }
    }

}

console.log(DP[T])