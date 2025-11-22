const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K, P, X] = input[0].split(' ').map(Number)

const check = Array.from(Array(10), () => Array(10).fill(0))
const num = {
    0 : [1, 1, 1, 1, 1, 1, 0],
    1 : [0, 0, 0, 0, 1, 1, 0],
    2 : [1, 0, 1, 1, 0, 1, 1],
    3 : [1, 0, 0, 1, 1, 1, 1],
    4 : [0, 1, 0, 0, 1, 1, 1],
    5 : [1, 1, 0, 1, 1, 0, 1],
    6 : [1, 1, 1, 1, 1, 0, 1],
    7 : [1, 0, 0, 0, 1, 1, 0],
    8 : [1, 1, 1, 1, 1, 1, 1],
    9 : [1, 1, 0, 1, 1, 1, 1]
}
for (let i = 0; i < 9; i++){
    for (let j = i + 1; j <= 9; j++){
        let cnt = 0
        for (let k = 0; k < 7; k++){
            if (num[i][k] !== num[j][k]) cnt++
        }

        check[i][j] = cnt
        check[j][i] = cnt
    }
}

let ans = 0

const now = String(X).padStart(K, '0')
for (let i = 1; i <= N; i++){
    const target = String(i).padStart(K, '0')
    
    if (now === target) continue
    
    let cnt = P
    let flag = 0

    for (let k = 0; k < K; k++){
        const [i, j] = [now[k], target[k]]
        cnt -= check[i][j]
        if (cnt < 0) {
            flag = 1
            break
        }
    }

    if (!flag) ans++
}

console.log(ans)