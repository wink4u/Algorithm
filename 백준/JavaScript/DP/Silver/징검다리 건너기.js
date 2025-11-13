const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const energy = input.slice(1, N).map((v) => v.split(' ').map(Number))
const k = Number(input[N])
const DP = Array.from(Array(N), () => Array(2).fill(Infinity))

DP[0][0] = 0;
DP[0][1] = Infinity;

for (let i = 1; i < N; i++) {
  DP[i][0] = Math.min(DP[i][0], DP[i - 1][0] + energy[i - 1][0]);
  DP[i][1] = Math.min(DP[i][1], DP[i - 1][1] + energy[i - 1][0]);

  if (i > 1) {
    DP[i][0] = Math.min(DP[i][0], DP[i - 2][0] + energy[i - 2][1]);
    DP[i][1] = Math.min(DP[i][1], DP[i - 2][1] + energy[i - 2][1]);
  }


  if (i > 2) {
    DP[i][1] = Math.min(DP[i][1], DP[i - 3][0] + k);
  }
}

console.log(Math.min(DP[N - 1][0], DP[N - 1][1]));