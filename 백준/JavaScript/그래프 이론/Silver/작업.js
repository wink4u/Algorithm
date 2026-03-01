const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const node = Array.from(Array(N + 1), () => [])

for (let i = 1; i <= M; i++){
    const [a, b] = input[i].split(' ').map(Number)
    node[b].push(a)
}

const x = input[M + 1]

const q = [x]
let idx = 0
let cnt = 0
const visit = Array(N + 1).fill(0)
visit[x] = 1

while (q.length > idx) {
    const now = q[idx++]

    for (const nxt of node[now]) {
        if (!visit[nxt]) {
            visit[nxt] = 1
            q.push(nxt)
            cnt++
        }
    }
}

console.log(cnt)