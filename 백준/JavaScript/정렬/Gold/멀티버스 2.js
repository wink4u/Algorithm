const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => input.push(line.trim())).on("close", () => {
  const [N, M] = input.shift().split(' ').map(Number)
  const space = {}
  for (let i = 0; i < N; i++){
    const v = input[i].split(' ').map(Number)
    const vSort = Array.from(new Set(v)).slice().sort((a, b) => b - a);
    
    const check = {}
    let cnt = 1

    for (let j = 0; j < vSort.length; j++){
      check[vSort[j]] = cnt
      cnt += 1
    }

    const tmp = [];
    for (let j = 0; j < M; j++){
      tmp.push(check[v[j]])
    }
    
    
    const value = tmp.join('')
    
    if (space[value]) space[value] += 1
    else space[value] = 1
  }

  let ans = 0

  Object.entries(space).forEach(([key, value]) => {
    if (value >= 2) {
      ans += Math.floor((value * (value - 1)) / (2))
    }
  })

  console.log(ans)
});
