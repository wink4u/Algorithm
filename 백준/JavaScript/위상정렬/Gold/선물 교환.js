const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const student = input.slice(1).map(v => v.split(' ').map(Number))
const visit = Array(N + 1).fill(0)

for (const [a, b] of student) {
    visit[a] += 1
    visit[b] += 1
}

const q = []

const remove = Array(N + 1).fill(0)

for (let i = 1; i <= N; i++){
    if (visit[i] < 2) {
        q.push(i)
        remove[i] = 1
    }
}

let idx = 0

while (q.length > idx) {
    const now = q[idx++]

    for (const nxt of student[now - 1]) {
        if (remove[nxt]) continue

        visit[nxt] -= 1

        if (visit[nxt] < 2) {
            q.push(nxt)
            remove[nxt] = 1
        }
    }
}


const ans = remove.reduce((acc, v, i) => {
    if (v === 0 && i > 0) acc.push(i)
    return acc
}, [])

if (ans.length) {
    console.log(ans.length)
    console.log(ans.join(' '))
} else {
    console.log(0)
}