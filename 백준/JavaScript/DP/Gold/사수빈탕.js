const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const [N, M] = input.shift().split(' ').map(Number)

    if (N === 0) {
        console.log(0);
        process.exit();
    }

    input = input.map((v) => v.split(' ').map(Number))
    const [x, y] = [
        Math.max(...input.map(([a]) => a)),
        Math.max(...input.map(([, b]) => b)),
    ];

    const dp = Array.from(Array(x + 1), () => Array(y + 1).fill(0))

    for (let i = 0; i < N; i++) {
        const [cx, cy] = input[i]
        dp[cx][cy] = M - (cx + cy) > 0 ? M - (cx + cy) : 0
    }

    for (let i = 0; i <= x; i++){
        for (let j = 0; j <= y; j++){
            const down = i > 0 ? dp[i - 1][j] : 0
            const left = j > 0 ? dp[i][j - 1] : 0

            dp[i][j] = dp[i][j] + Math.max(down, left)
        }
    }

    let ans = 0;

    for (let i = 0; i < N; i++){
        const [x, y] = input[i]
        ans = Math.max(ans, dp[x][y])
    }

    console.log(ans)
    process.exit()
})
