function solution(n, infection, edges, k) {
    var answer = 0;
    
    const check = []
    const node = Array.from(Array(n + 1), () => [])
    
    for (let i = 0; i < n - 1; i++){
        const [a, b, v] = edges[i]
        node[a].push([b, v])
        node[b].push([a, v])
    }
    
    const permutation = (arr, prev, cnt) => {    
        if (cnt === k) {
            check.push(arr.slice())
            return
        }
        
        for (let i = 1; i <= 3; i++){
            if (i !== prev) {
                arr.push(i)
                permutation(arr, i, cnt + 1)
                arr.pop()
            }
        }    
    }
    
    permutation([], -1, 0)
    
    for (let i = 0; i < check.length; i++){
        const visit = Array(n + 1).fill(0)
        const set = new Set()
        let cnt = 1
        
        visit[infection] = 1
        set.add(infection)
        
        for (let j = 0; j < k; j++){
            const v = check[i][j]
            let idx = 0
            
            const q = Array.from(set)
            
            while (q.length > idx) {
                const now = q[idx++]
                
                for (const [nxt, value] of node[now]) {
                    if (!visit[nxt] && v === value) {
                        q.push(nxt)
                        set.add(nxt)
                        visit[nxt] = 1
                    }
                }
            }
        }
        
        answer = Math.max(answer, set.size)
    }
    
    return answer;
}