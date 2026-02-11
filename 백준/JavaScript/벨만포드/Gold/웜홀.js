const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const T = Number(input[0])
let cnt = 0
let idx = 1

while (cnt < T) {
    const [N, M, W] = input[idx++].split(' ').map(Number)
    const road = input.slice(idx, idx + M + W).map(v => v.split(' ').map(Number))
    const node = []
    idx += M + W


    for (let i = 0; i < W + M; i++){
        let [s, e, t] = road[i]

        if (i >= M) {
            t = -t
        } else {
            node.push([e, s, t])
        }

        node.push([s, e, t])
    }

 
    const check = () => {
        const D = Array(N + 1).fill(90000000)
    
        D[1] = 0
        
        for (let i = 0; i < N; i++){
            for (let j = 0; j < node.length; j++){
                const [now, nxt, cost] = node[j]
    
                if (D[nxt] > D[now] + cost) {
                    D[nxt] = D[now] + cost
    
                    if (i === N - 1) return true 
                }
            }
        }

        return false

    }

    if (check()) console.log('YES')
    else console.log('NO')
    
    
    cnt++
}