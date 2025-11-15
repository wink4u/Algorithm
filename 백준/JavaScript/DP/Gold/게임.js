const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number)
const board = input.slice(1).map((v) => v.trim().split(''))

const visit = Array.from(Array(N), () => Array(M).fill(false))
const DP = Array.from(Array(N), () => Array(M).fill(0))

let max = -1

const isMove = (x, y, value) => {
    if (0 <= x && x < N && 0 <= y && y < M && board[x][y] !== 'H' && value + 1 > DP[x][y]){
        return true
    }
    return false
}
const dfs = (x, y, value) => {
    max = Math.max(max, value)    
    const move = Number(board[x][y])
    const d = [[x - move, y], [x + move, y], [x, y - move], [x, y + move]]

    for (const [nx, ny] of d){
        if (isMove(nx, ny, value)) {
            if (!visit[nx][ny]) {
                DP[nx][ny] = value + 1
                visit[nx][ny] = true
                dfs(nx, ny, value + 1)
                visit[nx][ny] = false
            } else {
                console.log(-1)
                process.exit()
            }
        }
    }
}

dfs(0, 0, 1)
console.log(max)
