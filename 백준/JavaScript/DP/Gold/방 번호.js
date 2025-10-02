const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
  
    const N = Number(input.shift())
    const arr = input.shift().split(' ').map(Number)
    const M = Number(input[0])
    const DP = Array(M + 1).fill(-1n)
    const maxBI = (a, b) => (a > b ? a : b);

    for (let i = N - 1; i >= 0; i--){
      const p = arr[i]
      const di = BigInt(i)

      for (let j = p; j <= M; j++){
        let cand = -1n;
        
        if (j === p) cand = maxBI(cand, di);

        if (DP[j - p] !== -1n) {
          cand = maxBI(cand, DP[j - p] * 10n + di);
        }

        if (cand !== -1n) {
          DP[j] = maxBI(DP[j], cand);
        }
      }
    }

    let best = -1n;
    for (let j = 0; j <= M; j++) best = maxBI(best, DP[j]);

    console.log(best.toString());
});
