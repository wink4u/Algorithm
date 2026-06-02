const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [M, N] = input[0].split(' ').map(Number)
const arr = input.slice(1, N + 1).map(v => v.split('').map(Number))
const [sy, sx] = input[N + 1].split(' ').map(Number)

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

let cnt = arr.flat().filter(v => v === 1).length - 1 
let date = 2

const q = [[sx - 1, sy - 1]]
const visit = Array.from(Array(N), () => Array(M).fill(0))
visit[sx - 1][sy - 1] = 1

while (q.length) {
    const len = q.length;

    for (let i = 0; i < len; i++){
        const [x, y] = q.shift()

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                if (!visit[nx][ny] && arr[nx][ny]) {
                    cnt--
                    visit[nx][ny] = 1
                    q.push([nx, ny])
                }
            }
        }
    }

    date++
}

console.log(date)
console.log(cnt)