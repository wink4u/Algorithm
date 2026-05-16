const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.trim().split(''))

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const isMove = (x, y) =>{
    return 0 <= x && x < N && 0 <= y && y < M
}
const bfs = (sx, sy) => {
    const visit = Array.from(Array(N), () => Array(M).fill(-1))
    visit[sx][sy] = 0

    const q = [[sx, sy]]
    let idx = 0
    let max = 0

    while (q.length > idx) {
        const [x, y] = q[idx++]
        
        max = Math.max(max, visit[x][y])

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (isMove(nx, ny) && arr[nx][ny] === 'L' && visit[nx][ny] === -1) {
                visit[nx][ny] = visit[x][y] + 1
                q.push([nx, ny])
            }
        }    
    }

    return max
}

let ans = 0

for (let i = 0; i < N; i++){
    for (let j = 0; j < M; j++){
        if (arr[i][j] === 'L') {
            ans = Math.max(ans, bfs(i, j))
        }
    }
}

console.log(ans)