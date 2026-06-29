const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split('').map(Number))
const visit = Array.from(Array(N), () => Array(N).fill(20000))

visit[0][0] = 0

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const bfs = () => {
    const q = []
    q.push([0, 0])
    
    while (q.length) {
        const [x, y] = q.shift()

        // if (x === N - 1 && y === N - 1) return visit[N - 1][N - 1]

        for (let d = 0; d < 4; d++){{
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (0 <= nx && nx < N && 0 <= ny && ny < N){
                if (arr[nx][ny] && visit[nx][ny] > visit[x][y]) {
                    q.push([nx, ny])
                    visit[nx][ny] = visit[x][y]
                } else if (!arr[nx][ny] && visit[nx][ny] > visit[x][y] + 1){
                    q.push([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1
                }
            }
        }}
    }

    return -1
}

bfs()
console.log(visit[N - 1][N - 1])