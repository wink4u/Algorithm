const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [R, C] = input[0].split(' ').map(Number)
let sx, sy, ex, ey
const arr = []

for (let i = 1; i <= R; i++) {
    const tmp = input[i].trim().split('')
    // console.log(tmp)
    for (let j = 0; j < C; j++){
        if (tmp[j] === '*') {
            ex = i - 1
            ey = j
        } else if (tmp[j] === 'K') {
            sx = i - 1
            sy = j
        }
    }

    arr.push(tmp)
}


const DP = Array.from(Array(R), () => Array(C).fill(Infinity))

const dx = [-1, 1, 0, 0, -1, -1, 1, 1]
const dy = [0, 0, -1, 1, -1, 1, -1, 1]

DP[sx][sy] = 0

let index = 0
q = []
q.push([sx, sy])

const check = (x, y) => {
    return 0 <= x && x < R && 0 <= y && y < C
}

while (q.length > index) {
    const [x, y] = q[index++]

    for (let d = 0; d < 8; d++){
        const nx = x + dx[d], ny = y + dy[d]

        if (check(nx, ny) && arr[nx][ny] !== '#') {
            if (d === 3 || d === 5 || d === 7) {
                if (DP[nx][ny] > DP[x][y]) {
                    DP[nx][ny] = DP[x][y]
                    q.push([nx, ny])
                }
            } else {
                if (DP[nx][ny] > DP[x][y] + 1) {
                    DP[nx][ny] = DP[x][y] + 1
                    q.push([nx, ny])
                }
            }

            
        }
    }
}

console.log(DP[ex][ey] === Infinity ? -1 : DP[ex][ey])