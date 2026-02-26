const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

let [N, M, K] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.split(' ').map(Number))
K = Math.min(K, N * N) - 1

const visit = Array.from(Array(N), () => Array(N).fill(0))
const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const isMove = (x, y) => {
    return 0 <= x && x < N && 0 <= y && y < N
}

const bfs = (i, j) => {
    const q = [[i, j]]
    let idx = 0
    let cnt = K

    while (q.length > idx) {
        const [x, y] = q[idx++]

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]
            if (isMove(nx, ny) && !arr[nx][ny] && !visit[nx][ny] && cnt) {
                visit[nx][ny] = 1
                q.push([nx, ny])
                cnt--
            }
        }
    }
}


let ans = M
for (let i = 0; i < N; i++){
    for (let j = 0; j < N; j++){
        if (ans) {
            if (!arr[i][j] && !visit[i][j]) {
                ans--
                visit[i][j] = 1
                bfs(i, j)
            }
        } else {
            if (!arr[i][j] && !visit[i][j]) {
                console.log('IMPOSSIBLE')
                process.exit()
            }

        }
    }
}

if (ans === M) {
    console.log('IMPOSSIBLE')
} else {
    console.log('POSSIBLE')
    console.log(ans)
}