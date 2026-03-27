const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const node = Array.from(Array(N + 1), () => [])
const outdegree = Array(N + 1).fill(0)

for (let i = 1; i <= M; i++){
    const [a, b] = input[i].split(' ').map(Number)
    node[b].push(a)
    outdegree[a]++
}

const q = []

for (let i = 1; i <= N; i++){
    if (!outdegree[i]) q.push(i)
}

let idx = 0
let ans = 0

while (idx < q.length) {
    const now = q[idx++]
    ans++

    for (const prev of node[now]) {
        outdegree[prev]--

        if (!outdegree[prev]) q.push(prev)
    }
}

console.log(ans)