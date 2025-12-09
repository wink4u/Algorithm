const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const T = Number(input[0])
let idx = 1

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const ans = []

for (let i = 0; i < T; i++){
    const [H, W, O, F, sx, sy, ex, ey] = input[idx++].split(' ').map(Number)
    const board = Array.from(Array(H + 1), () => Array(W + 1).fill(0))
    for (let i = 0; i < O; i++){
        const [x, y, v] = input[idx++].split(' ').map(Number)
        board[x][y] = v
    }


    const check = () => {
        const q = [[sx, sy, F]]
        const visit = Array.from(Array(H + 1), () => Array(W + 1).fill(-1))
        visit[sx][sy] = F
        let index = 0;
        
        while (q.length > index) {
            const [x, y, v] = q[index++]
    
            if (x === ex && y === ey) {
                return '잘했어!!'
            }

            if (v === 0) continue

            const now = board[x][y]
    
            for (let d = 0; d < 4; d++){
                const nx = x + dx[d]
                const ny = y + dy[d]
    
                if (1 <= nx && nx <= H && 1 <= ny && ny <= W){
                    const nxt = board[nx][ny]
                    
                    const vv = nxt - now

                    if (vv > 0 && v < vv) continue

                    if (v - 1 <= visit[nx][ny]) continue

                    visit[nx][ny] = v - 1
                    q.push([nx, ny, v - 1])
                }
            }
        }
        return '인성 문제있어??'
    }
    ans.push(check())
}

console.log(ans.join('\n'))