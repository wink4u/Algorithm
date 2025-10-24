const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [R, C] = input[0].split(' ').map(Number)
let board = []

const fire = []
let sx = 0, sy = 0
const visit = Array.from(Array(R), () => Array(C).fill(0))

for (let i = 1; i <= R; i++){
    const tmp = input[i].trim().split('')

    for (let j = 0; j < C; j++){
        if (tmp[j] === 'J') {
            sx = i -1
            sy = j
        } else if (tmp[j] === 'F'){
            fire.push([i - 1, j])
        }
    }

    board.push(tmp)
}

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const move = (x, y) => {
    if (0 <= x && x < R && 0 <= y && y < C) return true
    return false
}


const fireBfs = () => {
    const k = fire.length
    
    for (let i = 0; i < k; i++){
        const [x, y] = fire.shift()

        for (let d = 0; d < 4; d++){
            const nx = x + dx[d]
            const ny = y + dy[d]
            if (move(nx, ny)) {
                if(board[nx][ny] === '.' || board[nx][ny] === 'J') {
                    fire.push([nx, ny])
                    board[nx][ny] = 'F'
                }
            }
        }

    }
    
}

const bfs = () => {
    const q = [[sx, sy]]
    visit[sx][sy] = 1
    let cnt = 1

    while (q.length){
        const k = q.length
        fireBfs()

        for (let i = 0; i < k; i++){
            const [x, y] = q.shift()
        
            for (let d = 0; d < 4; d++){
                const nx = x + dx[d]
                const ny = y + dy[d]
                

                if (!move(nx, ny)) {
                    return cnt
                }

                if (!visit[nx][ny] && board[nx][ny] === '.') {
                    q.push([nx, ny])
                    visit[nx][ny] = 1
                }
                
            }
        }
        
        cnt++
    }

    return 'IMPOSSIBLE'
}

console.log(bfs())