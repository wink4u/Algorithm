const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K, Q, M] = input[0].split(' ').map(Number)
const student = input[1].split(' ').map(Number)
const code = input[2].split(' ').map(Number)
const DP = Array(N + 3).fill(0)


for (let i = 0; i < Q; i++){
    let v = code[i]

    if (student.includes(v)) continue

    let now = code[i]
    while (true) {
        DP[now] = 1
        now += v
        
        if (now > N + 2) break
    }
}

for (let i = 0; i < K; i++){
    if (DP[student[i]]) DP[student[i]] -= 1
}

for (let i = 3; i < N + 3; i++){
    DP[i] += DP[i - 1]
}


for (let i = 3; i < 3 + M; i++){
    const [s, e] = input[i].split(' ').map(Number)
    console.log(e - s + 1 - (DP[e] - DP[s - 1]))
}