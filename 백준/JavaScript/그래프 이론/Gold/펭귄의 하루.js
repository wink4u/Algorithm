const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.trim().split(''))

const isMove = (x, y) => {
    return 0 <= x && x < N && 0 <= y && y < M
}

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

let sx, sy, ex, ey

for (let i = 0; i < N; i++){
    for (let j = 0; j < M; j++){
        if (arr[i][j] === 'S') sx = i, sy = j
        else if (arr[i][j] === 'E') ex = i, ey = j
    }
}

const visit = Array.from(Array(N), () => Array.from(Array(M), () => Array(2).fill(-1)))
visit[sx][sy][0] = 0

const check = () => {
    const q = [[sx, sy, 0]]
    let idx = 0

    while (q.length > idx) {
        const [x, y, flag] =  q[idx++]
    
        for (let d = 0; d < 4; d++){
            const nx = x + dx[d], ny = y + dy[d]
            
            if (isMove(nx, ny) && arr[nx][ny] !== 'D') {
                if (!flag) {
                    if (arr[nx][ny] === 'F') {
                        if (visit[nx][ny][1] === -1) {
                            visit[nx][ny][1] = visit[x][y][0] + 1
                            q.push([nx, ny, 1])
                        }
                    } else {
                        if (visit[nx][ny][0] === -1) {
                            visit[nx][ny][0] = visit[x][y][0] + 1
                            q.push([nx, ny, 0])
                        }
                    }
                } else {
                    if (arr[nx][ny] === 'H') {
                        return visit[x][y][1] + 1
                    }

                    if (visit[nx][ny][1] === -1) {
                        visit[nx][ny][1] = visit[x][y][1] + 1
                        q.push([nx, ny, 1])
                    }
                }
            }
            
        }
    }

    return -1
}

console.log(check())