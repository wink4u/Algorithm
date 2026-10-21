function solution(h, grid, panels, seqs) {
    grid = grid.map(v => v.split(''))
    
    const [n, m] = [grid.length, grid[0].length]
    const k = panels.length
    const INF = 1e9
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    
    const bfs = (sx, sy) => {
        const visit = Array.from(Array(n), () => Array(m).fill(-1))
        visit[sx][sy] = 0
        const q = [[sx, sy]]
        
        for (let idx = 0; idx < q.length; idx++){
            const [x, y] = q[idx]
            
            for (let d = 0; d < 4; d++){
                const [nx, ny] = [x + dx[d], y + dy[d]]
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue
                if (grid[nx][ny] === '#' || visit[nx][ny] !== -1) continue
                
                visit[nx][ny] = visit[x][y] + 1
                q.push([nx, ny])
            
            }
        }
        return visit
    }
    
    let [eleX, eleY] = [0, 0]
    for (let i = 0; i < n; i++){
        for (let j = 0; j < m; j++){
            if (grid[i][j] === '@') [eleX, eleY] = [i, j]
        }
    }
    
    const eleVisit = bfs(eleX, eleY)
    const eleDistance = panels.map(([f, r, c]) => eleVisit[r - 1][c - 1])
    
    const distance = Array.from(Array(k), () => Array(k).fill(0))
    for (let i = 0; i < k; i++){
        const v = bfs(panels[i][1] - 1, panels[i][2] - 1)
        for (let j = 0; j < k; j++){
            if (i === j) continue
            distance[i][j] = panels[i][0] === panels[j][0]
                ? v[panels[j][1] - 1][panels[j][2] - 1]
                : eleDistance[i] + Math.abs(panels[i][0] - panels[j][0]) + eleDistance[j] 
            
        }
    }
    
    const node = Array.from(Array(k), () => [])
    const check = new Array(k).fill(0)
    for (const [a, b] of seqs) {
        node[a - 1].push(b - 1)
        check[b - 1]++
    }

    let answer = Infinity
    const visit = new Array(k).fill(false)
    const best = new Int32Array((1 << k) * k).fill(INF)
    const dfs = (now, mask, cost, cnt) => {
        if (cost >= answer) return
        if (cost >= best[mask * k + now]) return // 같은 상태에 더 싸게 온 적 있음
        best[mask * k + now] = cost

        if (cnt === k) {
            answer = cost
            return
        }

        for (let nxt = 0; nxt < k; nxt++) {
            if (visit[nxt] || check[nxt] > 0) continue

            visit[nxt] = true
            for (const v of node[nxt]) check[v]--

            dfs(nxt, mask | (1 << nxt), cost + distance[now][nxt], cnt + 1)

            for (const v of node[nxt]) check[v]++
            visit[nxt] = false
        }
    }

    dfs(0, 0, 0, 0)
    
    return answer;
}