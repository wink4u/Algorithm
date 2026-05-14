const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split("\n");

const [M, N, H] = input[0].split(' ').map(Number)
const tomato = input.slice(1).map(v => v.split(' ').map(Number))

const dx = [-1, 1, 0, 0, N, -N]
const dy = [0, 0, -1, 1, 0, 0]

const isMove = (x, y) => {
    return 0 <= x && x < N * H && 0 <= y && y < M
}

const bfs = () => {
    const q = []
    let idx = 0
    let zeroCnt = 0

    const visit = Array.from(Array(N * H), () => Array(M).fill(0))
    for (let i = 0; i < N * H; i++){
        for (let j = 0; j < M; j++){
            if (tomato[i][j] === 1) {
                q.push([i, j])
                visit[i][j] = 1
            } else if (tomato[i][j] === 0) {
                zeroCnt++
            }
        }
    }

    let cnt = 0
    let res = 0

    if (!zeroCnt) return 0

    while (q.length > idx) {
        const size = q.length - idx;

        for (let i = 0; i < size; i++) {
            const [x, y] = q[idx++];

            for (let d = 0; d < 6; d++) {
                const nx = x + dx[d];
                const ny = y + dy[d];

                if (d === 0 && nx % N === N - 1) continue;
                if (d === 1 && nx % N === 0) continue;

                if (
                    isMove(nx, ny) &&
                    tomato[nx][ny] === 0 &&
                    !visit[nx][ny]
                ) {
                    visit[nx][ny] = 1;
                    q.push([nx, ny]);
                    cnt++;
                }
            }
        }

        res++;

        if (cnt === zeroCnt) return res;
    }

    return -1
}

console.log(bfs())