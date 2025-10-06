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
  const isPrime = Array(10 ** 6 + 1).fill(true)
  isPrime[0] = isPrime[1] = false;

  for (let i = 2; i * i <= 10 ** 6; i++){
    if (isPrime[i]) {
      for (let j = i * i; j <= 10 ** 6; j += i){
        isPrime[j] = false;
      }
    }
  }

  const prime = []
  const checkIdx = Array(10 ** 6 + 1).fill(-1);
  const primeCnt = Array(10 ** 6 + 1).fill(0)
  let idx = -1;

  for (let i = 2; i <= 10 ** 6; i++){
    if (isPrime[i]) {
      idx++;
      prime.push(i)
    }

    checkIdx[i] = idx;
    primeCnt[i] = primeCnt[i - 1] + (isPrime[i] ? 1 : 0)
  }


  for (let i = 0; i < N; i++){
    const [s, e] = input[i].split(' ').map(Number)
    const cnt = primeCnt[e] - primeCnt[s - 1]

    if (cnt % 2 === 0) {
      console.log(-1)
      continue
    }

    const left = checkIdx[s - 1]
    const right = checkIdx[e]
    console.log(prime[left + Math.floor((right - left) / 2) + 1])
  }
});
