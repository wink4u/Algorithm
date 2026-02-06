const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.trim().split(''))

const dx = [1, 0]
const dy = [0, 1]

const check = (x, y) => {
    return 0 <= x && x < N && 0 <= y && y < M
}

const isBeach = (x, y, nx, ny) => {
    return (arr[x][y] === '.' && arr[nx][ny] === '#') || (arr[x][y] === '#' && arr[nx][ny] === '.')
}

let ans = 0
for (let x = 0; x < N; x++){
    let b = 0; l = 0;

    for (let y = 0; y < M; y++){
        for (let d = 0; d < 2; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (check(nx, ny) && isBeach(x, y, nx, ny)) {
                ans++
            }
        }

        if (x % 2) {
            const [nx, ny] = [x + 1, y + 1]

            if (check(nx, ny) && isBeach(x, y, nx, ny)) {
                ans++
            }
        } else {
            const [nx, ny] = [x + 1, y - 1]
            
            if (check(nx, ny) && isBeach(x, y, nx, ny)) {
                ans++
            }
        }

    }
}

console.log(ans)