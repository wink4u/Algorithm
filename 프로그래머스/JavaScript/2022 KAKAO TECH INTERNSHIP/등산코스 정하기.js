function solution(n, paths, gates, summits) {
    // 한 곳에서 출발하여 산봉우리 중 한곳만 방문한 뒤 다시 원래 출입구로 돌아와야함
    const node = Array.from(Array(n + 1), () => []);
    
    for (const [a, b, v] of paths){
        node[a].push([b, v])
        node[b].push([a, v])
    }
    
    const type = new Array(n + 1).fill(0)
    
    for (const gate of gates) type[gate] = 1
    for (const summit of summits) type[summit] = 2

    const check = (limit) => {
        const visit = new Array(n + 1).fill(0)
        const q = [];
        
        for (const gate of gates) {
            visit[gate] = 1
            q.push(gate)
        }
        
        let idx = 0;
        let best = Infinity;
        
        while (q.length > idx) {
            const now = q[idx++];
            
            for (const [nxt, cost] of node[now]) {
                if (cost > limit || visit[nxt]) continue
                
                visit[nxt] = 1
                
                if (type[nxt] === 2) {
                    best = Math.min(best, nxt)
                } else if (type[nxt] === 0) {
                    q.push(nxt)
                }
            }
        }
        
        return best === Infinity ? [false, 0] : [true, best]
    }
    
    // 다른 산봉우리 들리면 안됨
    let left = 1, right = 10000000

    while (left < right) {
        const mid = Math.floor((left + right) / 2)

        if (check(mid)[0]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    
    
    const [, summit] = check(left)
    
    return [summit, left];
}