const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => input.push(line.trim())).on("close", () => {
  const [N, M, K] = input.shift().split(" ").map(Number);
  const way = input.map((v) => v.split(" ").map(Number));
  const node = Array.from(Array(N + 1), () => [])
  const DP = Array.from(Array(N + 1), () => Array(N + 1).fill(-1))

  way.forEach(([a, b, c]) => {
    if (a < b) node[a].push([b, c])
  })

  DP[1][1] = 0

  for (let cnt = 1; cnt < M; cnt++){
    for (let now = 1; now <= N; now++){
      if (DP[now][cnt] === -1) continue

      for (const [nxt, value] of node[now]) {
        DP[nxt][cnt + 1] = Math.max(DP[nxt][cnt + 1], DP[now][cnt] + value)
      }
    }
  }

  let ans = 0;
  for (let i = 2; i <= M; i++){
    ans = Math.max(ans, DP[N][i])
  }

  console.log(ans)
});
