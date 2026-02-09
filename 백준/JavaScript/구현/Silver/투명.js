const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)

if (N === 0) {
    console.log(0)
    process.exit()
}

const visit = Array.from(Array(100), () => Array(100).fill(0))
let cnt = 0

for (let i = 1; i <= N; i++){
    const [sx, sy, ex, ey] = input[i].split(' ').map(Number)

    for (let j = sx - 1; j < ex; j++){
        for (let k = sy - 1; k < ey; k++){
            if (visit[j][k] > M) continue

            visit[j][k] += 1
            
            if (visit[j][k] > M) cnt++

        }
    }
}

console.log(cnt)