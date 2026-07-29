const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.split(' ').map(Number))
const node = Array.from(Array(N + 1), () => [])
const count = Array(N + 1).fill(0)

for (let i = 0; i < M; i++){
    const tmp = arr[i]
    for (let j = 1; j < tmp[0]; j++) {
        node[tmp[j]].push(tmp[j + 1])
        count[tmp[j + 1]]++
    }
}

const q = []
const ans = []
let cnt = 0

for (let i = 1; i <= N; i++){
    if (count[i] === 0) {
        ans.push(i)
        q.push(i)
    }
}

let idx = 0

while (q.length > idx) {
    const now = q[idx++]
    cnt++

    for (const nxt of node[now]) {
        count[nxt]--

        if (count[nxt] === 0) {
            ans.push(nxt)
            q.push(nxt)
        }
    }
}

console.log(cnt !== N ? 0 : ans.join('\n'))