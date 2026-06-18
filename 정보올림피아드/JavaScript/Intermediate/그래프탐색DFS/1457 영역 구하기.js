const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [N, M, K] = input[0].split(' ').map(Number)
const info = input.slice(1).map(v => v.split(' ').map(Number))

const square = Array.from(Array(N), () => Array(M).fill(0))


const fillSquare = (sx, sy, ex, ey) => {
    for (let i =  sy; i < ey; i++){
        for (let j = sx; j < ex; j++){
            square[i][j] = 1
        }
    }
}

for (let i = 0; i < K; i++){
    fillSquare(...info[i])
}

const visit = Array.from(Array(N), () => Array(M).fill(0))
const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const isMove = (x, y) => {
    return 0 <= x && x < N && 0 <= y && y < M
}

const bfs = (sx, sy) => {
    const q = [[sx, sy]]
    let cnt = 1

    while (q.length) {
        const [x, y] = q.shift()

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (isMove(nx, ny) && !square[nx][ny] && !visit[nx][ny]) {
                visit[nx][ny] = 1
                cnt++
                q.push([nx, ny])
            }
        }
    }

    return cnt
}

const ans = []

for (let i = 0; i < N; i++){
    for (let j = 0; j < M; j++){
        if (!square[i][j] && !visit[i][j]) {
            visit[i][j] = 1
            ans.push(bfs(i, j))
        }
    }
}

console.log(ans.length)
console.log(ans.sort((a, b) => a - b).join(' '))
