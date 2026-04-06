const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))

const DP = Array.from(Array(N), () => Array(1 << N).fill(-1))

const dfs = (now, visit) => {
    if (visit === (1 << N) - 1){
        return arr[now][0] ? arr[now][0] : Infinity
    }

    if (DP[now][visit] !== -1) return DP[now][visit]

    DP[now][visit] = Infinity
    
    for (let i = 1; i < N; i++){
        if (!arr[now][i]) continue

        if (visit & (1 << i)) continue

        DP[now][visit] = Math.min(DP[now][visit], dfs(i, visit | (1 << i)) + arr[now][i])
    }

    return DP[now][visit]
}

console.log(dfs(0, 1))