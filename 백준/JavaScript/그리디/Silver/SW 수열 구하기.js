const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
    const N = input[0];
    let [l, r] = [1, N]
    const ans = []

    while (l < r) {
        ans.push(l)
        ans.push(r)

        l += 1
        r -= 1
    }

    if (l === r) ans.push(l)
    
    
    console.log(ans.join(' '))

});
