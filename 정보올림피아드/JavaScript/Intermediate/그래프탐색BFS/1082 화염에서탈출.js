const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [R, C] = input[0].split(' ').map(Number)
const board = input.slice(1).map(v => v.trim().split(''))

let sx, sy

// '.' empty '*' fire 'X' rock 'D' house


const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const fire = []

const isMove = (x, y) => {return 0 <= x && x < R && 0 <= y && y < C}

for (let i = 0; i < R; i++){
    for (let j = 0; j < C; j++){
        if (board[i][j] === 'S') sx = i, sy = j
        else if (board[i][j] === '*') fire.push([i, j])
    }
}

const fireBfs = () => {
    const fireCnt = fire.length
    let cnt = 0
    
    while (cnt < fireCnt) {
        const [x, y] = fire.shift()

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (isMove(nx, ny)) {
                if (board[nx][ny] === '.' || board[nx][ny] === 'S') {
                    board[nx][ny] = '*'
                    fire.push([nx, ny])
                }
            }
        }

        cnt++
    }
}


const q = [[sx, sy]]
const visit = Array.from(Array(R), () => Array(C).fill(-1))
visit[sx][sy] = 0

const humanBfs = () => {
    while (q.length) {
        const len = q.length

        for (let i = 0; i < len; i++) {

            const [x, y] = q.shift()

            if (board[x][y] === '*') continue

            for (let d = 0; d < 4; d++){
                const [nx, ny] = [x + dx[d], y + dy[d]]

                if (isMove(nx, ny) && visit[nx][ny] === -1) {
                    if (board[nx][ny] === '.') {
                        q.push([nx, ny])
                        visit[nx][ny] = visit[x][y] + 1
                    } else if (board[nx][ny] === 'D') return visit[x][y] + 1
                } 
            }
        }

        fireBfs()
    
    }

    return 'impossible'
}

console.log(humanBfs())