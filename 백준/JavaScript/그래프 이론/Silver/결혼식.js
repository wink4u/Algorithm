const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const M = Number(input[1])
const arr = input.slice(2).map(v => v.split(' ').map(Number))

let ans = 0

const visit = Array(N + 1).fill(0)
const node = Array.from(Array(N + 1), () => [])


for (const [a, b] of arr) {
    node[a].push(b)
    node[b].push(a)
}

visit[1] = 1

const q = [1]
let idx = 0

while (q.length > idx) {
    const now = q[idx++]

    
    const v = visit[now]

    for (const nxt of node[now]) {
        if (!visit[nxt] && visit[now] + 1 < 4) {
            visit[nxt] = visit[now] + 1
            q.push(nxt)
            ans++
        }
    }
}


console.log(ans)
