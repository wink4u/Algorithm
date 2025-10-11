const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(line.trim())
})
.on("close", () => {
  const N = Number(input.shift())
  input = input.map((v) => Number(v))
  const gcd = (a, b) => {
    return b === 0 ? a : gcd(b, a % b);
  }

  const arr = []

  for (let i = 1; i < N; i++){
    arr.push(input[i] - input[i - 1])
  }

  let v = 0;

  for (let i = 1; i < N - 1; i++){
    if (!v) v = gcd(arr[i], arr[i - 1])
    else {
      const tmp = gcd(v, arr[i])
      v = tmp
    }
  }

  let ans = 0;

  for (let i = 0; i < arr.length; i++){
    if (v !== arr[i]){
      ans += Math.floor(arr[i] / v) - 1
    }
  }

  console.log(ans)
});
