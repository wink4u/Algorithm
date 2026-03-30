const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const node = Array.from(Array(26), () => [])
const value = Array(26).fill(0)
const indegree = Array(26).fill(0)
const visit = Array(26).fill(false)
const DP = Array(26).fill(0)

for (let i = 0; i < input.length; i++){
    const [A, cost, arr = ''] = input[i].trim().split(' ')
    const aNum = A.charCodeAt() - 65
    value[aNum] = Number(cost)
    visit[aNum] = true

    for (const B of arr) {
        const bNum = B.charCodeAt() - 65

        node[bNum].push(aNum)
        indegree[aNum]++
        visit[bNum] = true
    }
}

const q = []

for (let i = 0; i < 26; i++){
    if (visit[i] && !indegree[i]) {
        q.push(i)
        DP[i] = value[i]
    }
}

let idx = 0

while (idx < q.length) {
    const now = q[idx++]

    for (const nxt of node[now]) {
        DP[nxt] = Math.max(DP[nxt], DP[now] + value[nxt])
        indegree[nxt]--;

        if (!indegree[nxt]) q.push(nxt)
    }
}

console.log(Math.max(...DP))