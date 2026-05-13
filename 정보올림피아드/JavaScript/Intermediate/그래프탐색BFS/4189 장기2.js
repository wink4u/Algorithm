const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const [r, c, s, k] = input[1].split(' ').map(Number)

const dx = [1, 1, 2, 2, -1, -1, -2, -2]
const dy = [2, -2, 1, -1, 2, -2, 1, -1]

const q = [[r, c]]
let idx = 0

const visit = Array.from(Array(N + 1), () => Array(M + 1).fill(Infinity))
visit[r][c] = 0

console.log(visit[r][c])

while (q.length > idx) {
    const [x, y] = q[idx++]

    if (x === s && y === k) break

    for (let d = 0; d < 8; d++){
        const [nx, ny] = [x + dx[d], y + dy[d]]

        if (1 <= nx && nx <= N && 1 <= ny && ny <= M) {
            if (visit[nx][ny] > visit[x][y] + 1) {
                visit[nx][ny] = visit[x][y] + 1
                q.push([nx, ny])
            }
        }
    }
}

console.log(visit[s][k])