const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.trim().split(''))
const DP = Array.from(Array(N), () => Array(M).fill(-1))
let ans = -1

const check = (x, y, flag) => {
    for (let d = 0; d < 3; d++){
        const nx = x + dx[d], ny = y + dy[d]
        if (isRight(nx, ny) && DP[nx][ny] !== -1) {
            DP[x][y] = Math.max(DP[x][y], DP[nx][ny] + flag)
        }
    }

}

const isRight = (x, y) => {
    return 0 <= x && x < N && 0 <= y && y < M
}

const dx = [-1, 0, 1]
const dy = [-1, -1, -1]

for (let j = 0; j < M; j++){
    for (let i = 0; i < N; i++){
        if (arr[i][j] === 'R') {
            DP[i][j] = 0
        } else if (arr[i][j] === 'C') {
            check(i, j, 1)
        } else if (arr[i][j] === 'O' || arr[i][j] === '.') {
            check(i, j, 0)

            if (arr[i][j] === 'O'){
                ans = Math.max(ans, DP[i][j])
            }
        }
    }
}

console.log(ans)