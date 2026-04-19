const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M, K] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.trim().split(''))
const rsp = ['R', 'S', 'P']
let ans = null;

const fight = (a, b) => {
    if (a === 'R' && b === 'S') return true
    if (a === 'S' && b === 'P') return true
    if (a === 'P' && b === 'R') return true


    return false
}

const dfs = (idx, alive, seq) => {
    // 성공
    if (alive.length <= K) {
        const str = seq.join('')
        if (!ans || str.length < ans.length || (str.length === ans.length && str < ans)) {
            ans = str
        }
        return
    }

    // 끝
    if (idx === M) return

    // 가지치기 (중요)
    if (ans && seq.length >= ans.length) return

    for (let i = 0; i < 3; i++) {
        const now = rsp[i]

        const nextAlive = []

        for (const j of alive) {
            if (!fight(now, arr[j][idx])) {
                nextAlive.push(j)
            }
        }

        seq.push(now)
        dfs(idx + 1, nextAlive, seq)
        seq.pop()
    }
}

const init = Array.from({ length: N }, (_, i) => i)

dfs(0, init, [])

if (!ans){
    console.log(-1)
} else {
    console.log(ans.length)
    console.log(ans)
}