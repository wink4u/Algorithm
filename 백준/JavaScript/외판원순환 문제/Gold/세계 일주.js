const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))
const DP = Array.from(Array(N), () => Array(1 << N).fill(-1))

const trip = Array.from(Array(N), () => Array(N).fill(0))

const distance = (x1, y1, x2, y2) => {
    return Math.sqrt(Math.abs(x1 - x2) ** 2 + Math.abs(y1 - y2) ** 2)
}
for (let i = 0; i < N - 1; i++){
    const [ix, iy] = arr[i]
    for (let j = i + 1; j < N; j++){
        const [jx, jy] = arr[j]
        const v = distance(ix, iy, jx, jy)

        trip[i][j] = v
        trip[j][i] = v
    }
}

const dfs = (now, visit) => {
    if (visit === (1 << N) - 1){
        return trip[now][0] ? trip[now][0] : Infinity
    }

    if (DP[now][visit] !== -1) return DP[now][visit]

    DP[now][visit] = Infinity

    for (let i = 1; i < N; i++){
        if (!trip[now][i]) continue

        if (visit & (1 << i)) continue

        DP[now][visit] = Math.min(DP[now][visit], dfs(i, visit | (1 << i)) + trip[now][i])
    }

    return DP[now][visit]
}

const ans = dfs(0, 1)
console.log(ans === Infinity ? -1 : ans)