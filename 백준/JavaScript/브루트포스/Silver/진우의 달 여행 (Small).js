const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number)
const board = input.slice(1).map((v) => v.split(' ').map(Number))

dx = [1, 1, 1]
dy = [-1, 0, 1]

let min = Infinity
const dfs = (prev, x, y, v) => {
    if (x === N - 1) {
        min = Math.min(min, v)
        return
    }

    for (let d = 0; d < 3; d++){
        if (prev !== d) {
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (0 <= nx && nx < N && 0 <= ny && ny < M){
                dfs(d, nx, ny, board[nx][ny] + v)
            }
        }
    }
}

for (let i = 0; i < M; i++){
    dfs(-1, 0, i, board[0][i])
}

console.log(min)