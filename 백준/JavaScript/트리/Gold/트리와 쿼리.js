const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, R, Q] = input[0].split(' ').map(Number)
const info = input.slice(1, N).map((v) => v.split(' ').map(Number))
const arr = input.slice(N).map(Number)
const node = Array.from(Array(N + 1), () => [])

const visit = Array(N + 1).fill(false)
const DP = Array(N + 1).fill(1)

for (let i = 0; i < N - 1; i++){
  const [u, v] = info[i]
  node[u].push(v)
  node[v].push(u)
}

const dfs = (now) => {
  if (visit[now]) return DP[now]
  visit[now] = true

  for (const nxt of node[now]){
    if (visit[nxt]) continue
    DP[now] += dfs(nxt)
  }

  return DP[now]
}

dfs(R)

const ans = [];
for (const u of arr) {
  ans.push(DP[u])
}

console.log(ans.join('\n'))