const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const node = Array.from(Array(N + 1), () => [])
const check = Array(N + 1).fill(0)

for (let i = 1; i <= M; i++){
    const [a, b] = input[i].split(' ').map(Number)
    node[a].push(b)
    check[b] += 1
}

const q =[]

for (let i = 1; i <= N; i++){
    if (check[i] == 0) q.push(i)
}

const ans = []

while (q.length) {
    const now = q.shift()
    ans.push(now)

    for (const nxt of node[now]) {
        check[nxt] -= 1

        if (check[nxt] === 0) {
            q.push(nxt)
        }
    }
}

console.log(ans.join(' '))