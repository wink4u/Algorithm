const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
    const N = Number(input.shift())
    const cakes = input.map((v) => v.split(' ').map(Number).reverse())

    const DP = Array.from(Array(N + 1), () => Array(5).fill(Infinity))
    
    const dx = [0, -1, 1, 0, 0]
    const dy = [0, 0, 0, -1, 1]

    DP[0][0] = 0
    for (let i = 1; i <= 4; i++) {
        DP[0][i] = 1
    }


    for (let i = 1; i <= N; i++){
        for (let d = 0; d <= 4; d++){
            const [x, y] = [cakes[i][0] + dx[d],  cakes[i][1] + dy[d]]

            for (let j = 0; j <= 4; j++){
                const [nx, ny] = [cakes[i - 1][0] + dx[j], cakes[i - 1][1] + dy[j]]
                DP[i][d] = Math.min(DP[i][d], Math.abs(nx - x) + Math.abs(ny - y) + DP[i - 1][j])
            }
        }
    }

    console.log(Math.min(...DP[N]))
});
