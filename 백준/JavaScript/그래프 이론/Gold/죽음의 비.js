const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, H, D] = input[0].split(" ").map(Number);
const board = input.slice(1).map((v) => v.trim().split(''));

let sx = 0, sy = 0
for (let i = 0; i < N; i++){
    let flag = 0
    for (let j = 0; j < N; j++){
        if (board[i][j] === 'S') {
            sx = i, sy = j
            flag = 1
            break
        }
    }

    if (flag) break
}

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const bfs = () => {
    const q = [[sx, sy, 0, H, 0]]
    const visit = Array.from(Array(N), () => Array(N).fill(-1))
    visit[sx][sy] = H
    let idx = 0

    while (q.length > idx){
        const [x, y, cnt, hp, umb] = q[idx++]
        

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                let tmpUm = umb, tmpHp = hp
                if (board[nx][ny] === 'E') return cnt + 1

                if (board[nx][ny] === 'U') tmpUm = D

                if (tmpUm) tmpUm -= 1
                else tmpHp -= 1

                if (tmpHp === 0) continue
                
                
                const v = tmpUm + tmpHp

                if (v <= visit[nx][ny]) continue

                visit[nx][ny] = v
                q.push([nx, ny, cnt + 1, tmpHp, tmpUm])
            }
        }
    }

    return -1
}


console.log(bfs())