const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))
let ans = Infinity


const dfs = (cnt, now, visit, total) => {
    if (cnt === N) {
        ans = Math.min(total, ans)
        return
    }

    if (total > ans) return
    
    for (let nxt = 0; nxt < N; nxt++){
        if (nxt === 0 && cnt !== N - 1) continue
        const v = arr[now][nxt]

        if (v) {
            if (nxt !== now && !visit[nxt]) {
                visit[nxt] = true
                dfs(cnt + 1, nxt, visit, total + v)
                visit[nxt] = false
            }
        }
    }
}

dfs(0, 0, Array(N).fill(false), 0)
console.log(ans)
