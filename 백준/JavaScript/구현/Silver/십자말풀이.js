const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const arr = input.slice(1).map((v) => v.trim().split(''))
const ans = []

const check = (x, y) => {
    if (y === 0 || (arr[x][y - 1] === '#')) {
        let cnt = 1
        let ny = y + 1
        while (ny < M) {
            if (arr[x][ny] === '#') {
                break
            }

            ny++
            cnt++

            if (cnt >= 3) return true
        }
    }


    if (x === 0 || arr[x - 1][y] === '#') {
        let cnt = 1
        let nx = x + 1

        while (nx < N) {
            if (arr[nx][y] === '#') {
                break
            }

            nx++
            cnt++

            if (cnt >= 3) return true
        }
    }

    return false
}




for (let i = 0; i < N; i++){
    for (let j = 0; j < M; j++){
        if (arr[i][j] === '.' && check(i, j)) {
            ans.push([i + 1, j + 1])
        }
    }
}

console.log(ans.length)
console.log(ans.map((v) => v.join(' ')).join('\n'))