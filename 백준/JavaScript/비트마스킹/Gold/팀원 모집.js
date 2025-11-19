const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number)
const check = Array(M).fill(0)

let target = 0

for (let i = 0; i < N; i++){
    target |= (1 << i)
}

for (let i = 0; i < M; i++){
    const friends = input[i + 1].trim().split(' ').slice(1).map(Number)
    
    let tmp = check[i] === 0 ? 0 : check[i]

    for (const friend of friends){
        tmp |= (1 << (friend - 1))
    }

    check[i] = tmp
}


let ans = Infinity
const dfs = (idx, cnt, total) => {
    if (total === target) {
        ans = Math.min(ans, cnt)
        return
    }

    if (idx >= M) return

    dfs(idx + 1, cnt + 1, total | check[idx])
    dfs(idx + 1, cnt, total)
}

dfs(0, 0, 0)
console.log(ans === Infinity ? -1 : ans)