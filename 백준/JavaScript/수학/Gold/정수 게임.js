const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
    const [N, K] = input.shift().split(' ').map(Number)
    let arr = input[0].split(' ').map(Number)
    arr = Array.from(new Set(arr))
    arr.sort((a, b) => a - b)
    
    if (arr[0] === 1) {
      console.log(0)
      process.exit()
    }

    const gcd = (a, b) => {
      while (b > 0){
        const tmp = a % b
        a = b
        b = tmp
      }
      return a
    }

    const lcm = (curr, x) => {
      const g = gcd(curr, x)
      const v = Math.floor(curr / g);

      if (v > Math.floor(N / x)) return N + 1
      return v * x
    }

    let ans = 0;

    const dfs = (idx, currLcm, sign) => {
      for (let i = idx; i < arr.length; i++){
        const L = lcm(currLcm, arr[i])
        if (L > N) continue;
        ans += sign * Math.floor(N / L);
        dfs(i + 1, L, -sign)
      }
    }

    dfs(0, 1, 1)
    console.log(N - ans)
});
