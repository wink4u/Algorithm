const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0]);
const stone = input.slice(1).map(v => v.split(' ').map(Number))
const omok = Array.from(Array(20), () => Array(20).fill(-1))

function isMove (x, y) {
    return 1 <= x && x < 20 && 1 <= y && y < 20
}

const direction = (start, sx, sy) => {
    const dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    const dy = [0, 0, -1, 1, -1, 1, 1, -1]
    
    let cnt = 1;
    const visit = Array.from(Array(20), () => Array(20).fill(0))
    visit[sx][sy] = 1

    const k = omok[sx][sy]
    const q = [[sx, sy]]
    let idx = 0

    while (q.length > idx) {
        const [x, y] = q[idx++]

        for (let d = start; d < start + 2; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]
        
            if (isMove(nx, ny) && omok[nx][ny] === k && !visit[nx][ny]) {
                visit[nx][ny] = 1
                q.push([nx, ny])
                cnt++
            }
        }

    }


    if (cnt === 5) {
        return true
    }

    return false
}

const check = (x, y) => {
    for (let i = 0; i < 8; i += 2){
        if (direction(i, x, y)) return true
    }

    return false
}


let ans = -1

if (N < 10) {
    console.log(-1)
    process.exit()
}

for (let i = 0; i < N; i++){
    const [x, y] = stone[i]
    if (i % 2) {
        omok[x][y] = 1
    } else {
        omok[x][y] = 2
    }


    if (i >= 9) {
        if (check(x, y)) {
            ans = i + 1
            break
        }
    }
}


console.log(ans)