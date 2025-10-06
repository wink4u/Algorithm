const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const a = [], b = [], c = [], d = [];
let cnt = 0;
let N;
rl.on("line", (line) => {
  if (cnt === 0) {
    N = Number(line.trim())
    cnt += 1
  } else {
    const v = line.trim().split(' ').map(Number)
    a.push(v[0])
    b.push(v[1])
    c.push(v[2])
    d.push(v[3])
  }
})
  .on("close", () => {
    const map = new Map();

    for (let i = 0; i < N; i++){
      for (let j = 0; j < N; j++){
        const one = a[i] + b[j]
        map.set(one, (map.get(one) || 0) + 1);
      }
    }

    let ans = 0;

    for (let i = 0; i < N; i++){
      for (let j = 0; j < N; j++){
        const v = c[i] + d[j]
        if (map.has(-v)) ans += map.get(-v)
      }
    }

    console.log(ans)
});
