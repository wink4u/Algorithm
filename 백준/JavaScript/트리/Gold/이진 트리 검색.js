const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(Number(line)))
  .on("close", () => {

    const dfs = (f, e) => {
      if (f > e) return

      let m = e + 1

      for (let i = f + 1; i <= e; i++){
        if (input[f] < input[i]){
          m = i
          break
        }
      }

      dfs(f + 1, m - 1)
      dfs(m, e)
      console.log(input[f])
    }

    dfs(0, input.length - 1)
});
