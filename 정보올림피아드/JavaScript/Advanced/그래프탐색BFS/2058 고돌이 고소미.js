const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const [asx, asy, aex, aey] = input[1].split(' ').map(Number)
const [bsx, bsy, bex, bey] = input[2].split(' ').map(Number)

const arr = input.slice(3).map(v => v.split(' ').map(Number))
const visit = Array.from(Array(N), () => 
    Array.from(Array(N), () => 
        Array.from(Array(N), () => Array(N).fill(0))
    )
)

const isMove = (ax, ay, bx, by) => {
    return 0 <= ax && 0 <= bx && ax < N && bx < N && 0 <= ay && 0 <= by && ay < N && by < N
}

const isMeet = (ax, ay, bx, by) => {
    return (Math.abs(ax - bx) <= 1 && Math.abs(ay - by) <= 1)
}

const check = (ax, ay, bx, by) => {
    if (!isMove(ax, ay, bx, by)) return false

    if (visit[ax][ay][bx][by] || arr[ax][ay] || arr[bx][by]) return false

    if (isMeet(ax, ay, bx, by)) return false

    return true
}

const dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
const dy = [0, 0, -1, 1, -1, 1, -1, 1, 0]

const bfs = () => {
    const q = []
    q.push([asx - 1, asy - 1, bsx - 1, bsy - 1, 0])
    visit[asx - 1][asy - 1][bsx - 1][bsy - 1] = 1
    let idx = 0

    while (q.length > idx) {
        const [ax, ay, bx, by, v] = q[idx++]

        if (ax === aex - 1 && ay === aey - 1 && bx == bex -1 && by === bey - 1) {
            return v
        }


        for (let i = 0; i < 9; i++){
            const [nax, nay] = [ax + dx[i], ay + dy[i]]
            for (let j = 0; j < 9; j++){
                const [nbx, nby] = [bx + dx[j], by + dy[j]]

                if (check(nax, nay, nbx, nby)) {
                    q.push([nax, nay, nbx, nby, v + 1])
                    visit[nax][nay][nbx][nby] = 1
                }
            }
        }
    }

    return -1
}

console.log(bfs())
