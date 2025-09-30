const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
    const [N, R, D, x, y] = input.shift().split(' ').map(Number)
    const top = input.map((v) => v.split(' ').map(Number))
    const node = Array.from(Array(N), () => [])
    const visit = Array(N).fill(false)
    let q = []

    const dist = (x1, y1, x2, y2) => {
      const dx = x1 - x2, dy = y1 - y2
      return dx * dx + dy * dy <= R * R

    }
    for (let i = 0; i < N; i++){
      const [ix, iy] = top[i]
      if (dist(ix, iy, x, y)){
        visit[i] = true
        q.push([i, D])
      }

      for (let j = i + 1; j < N; j++){
        if (i !== j){
          const [jx, jy] = top[j]
  
          if (dist(ix, iy, jx, jy)){
            node[i].push(j)
            node[j].push(i)
          }
        }
      }
    }

    let ans = 0;

    while (q.length) {
      const [nowTop, value] = q.shift()
      ans += value

      for (const nxt of node[nowTop]){
        if (visit[nxt] === false){
          q.push([nxt, value / 2])
          visit[nxt] = true
        }
      }
    }

    const check = (num) => {
      const str = num.toString();

      if (Number.isInteger(num)) return num.toFixed(1)

      const [, decimal = ""] = str.split(".")

      if (decimal.length <= 2) {
        return num
      } else {
        return num.toFixed(2)
      }
    }

    console.log(check(ans))
});
