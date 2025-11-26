const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const board = input.slice(1).map((v) => v.split(' ').map(Number))


for (let k = 0; k < N; k++){
    for (let i = 0; i < N; i++){
        for (let j = 0; j < N; j++){
            if (board[i][k] && board[k][j]) {
                board[i][j] = 1
            }
        }
    }
}


board.map((v) => console.log(v.join(' ')))