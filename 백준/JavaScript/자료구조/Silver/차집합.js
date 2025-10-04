const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => input.push(line.trim())).on("close", () => {
  const [N, M] = input.shift().split(' ').map(Number)
  const A = input[0].split(' ').map(Number)
  const B = input[1].split(' ').map(Number)

  const check = {}

  for (let i = 0; i < M; i++){
    check[B[i]] = true
  }

  const ans = [];

  for (let i = 0; i < N; i++){
    if (check[A[i]]) continue;
    ans.push(A[i])
  }

  ans.sort((a, b) => a - b);
  
  if (ans.length) {
    console.log(ans.length)
    console.log(ans.join(' '))
  }else {
    console.log(0)
  }
});
