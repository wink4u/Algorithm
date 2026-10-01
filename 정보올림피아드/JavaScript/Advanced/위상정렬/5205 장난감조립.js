const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const M = Number(input[1])
const node = Array.from(Array(N + 1), () => [])
const DP = Array.from(Array(N + 1), () => Array(N + 1).fill(0))
const check = Array(N + 1).fill(0)

input.slice(2).forEach((v) => {
    const [x, y, k] = v.split(' ').map(Number)
    node[y].push([x, k])
    check[x] += 1
})

const q =[]
for (let i = 1; i <= N; i++){
    if (check[i] == 0) q.push(i)
}

while (q.length) {
    const now = q.shift()
    
    for (const [nxt, nxtValue] of node[now]){
        const total = DP[now].filter(e => 0 === e).length;
        if (total === N + 1) DP[nxt][now] += nxtValue
        else {
            for (let i = 0; i <= N; i++){
                DP[nxt][i] += DP[now][i] * nxtValue
            }
        }

        check[nxt] -= 1
        if (check[nxt] == 0) q.push(nxt)
    }
}

for (let i = 1; i <= N; i++){
    if (DP[N][i] > 0) console.log(i, DP[N][i])
}