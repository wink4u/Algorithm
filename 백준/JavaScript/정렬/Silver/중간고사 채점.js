const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const score = input[1].split(' ').map(Number)
const arr = input.slice(2).map(v => v.trim().split(' '))
const ans = []

for (let i = 0; i < M; i++){
    const num = Number(arr[i][0])
    let cnt = 0

    for (let j = 0; j < N; j++){
        if (arr[i][j + 1] === 'O') cnt += score[j]
    }

    ans.push([num, cnt])
}


ans.sort((a, b) => {
    if (a[1] !== b[1]) return b[1] - a[1]
    if (a[0] !== b[0]) return a[0] - b[0]
})

console.log(ans[0].join(' '))