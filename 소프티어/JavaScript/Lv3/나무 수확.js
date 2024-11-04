const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];
rl.on('line', function(line){
    input.push(line.split(' ').map(Number))
}).on('close', function(){
    let n = input[0][0]
    const board = input.slice(1);
    const DP = Array.from(Array(n), () => Array(n).fill(0));
    const RDP = Array.from(Array(n), () => Array(n).fill(0));
    const dx = [0, 1]
    const dy = [1, 0]
    const rdx = [-1, 0]
    const rdy = [0, -1]

    DP[0][0] = board[0][0]
    RDP[n - 1][n - 1] = board[n - 1][n - 1]
    let res = 0;
    
    for (let x = 0; x < n; x++){
        for (let y = 0; y < n; y++){
            for (let d = 0; d < 2; d++){
                const [nx, ny] = [x + dx[d], y + dy[d]]
                if (0 <= nx && nx < n && 0 <= ny && ny < n){
                    if (DP[nx][ny] <= DP[x][y] + board[nx][ny]){
                        DP[nx][ny] = DP[x][y] + board[nx][ny]
                    }
                }
            }
        }
    }

    for (let x = n - 1; x >= 0; x--){
        for (let y = n - 1; y >= 0; y--){
            for (let d = 0; d < 2; d++){
                const [nx, ny] = [x + rdx[d], y + rdy[d]]
                if (0 <= nx && nx < n && 0 <= ny && ny < n){
                    if (RDP[nx][ny] <= RDP[x][y] + board[nx][ny]){
                        RDP[nx][ny] = RDP[x][y] + board[nx][ny]
                    }
                }
            }

            res = Math.max(res, DP[x][y] + RDP[x][y])
        }
    }

    console.log(res);
})