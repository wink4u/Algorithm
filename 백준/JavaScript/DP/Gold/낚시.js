const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number)
const board = input.slice(1, N + 1).map((v) => v.split(' ').map(Number))
const Q = input.slice(N + 1).map((v) => v.split(' ').map(Number))


for (let i = 0; i < M; i++){
    for (let j = 1; j < N; j++){
        board[j][i] += board[j - 1][i]

        if (i > 0) {
            board[j][i] += board[j - 1][i - 1]
            if (j > 1) board[j][i] -= board[j - 2][i - 1]
        }
            
    }
}

const ans = []

Q.forEach((v) => {
    const [x, y] = v
    ans.push(board[x - 1][y - 1])
})

console.log(ans.join('\n'))