/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var minScore = function(n, roads) {
    const node = Array.from(Array(n + 1), () => [])

    for (const [u, v, w] of roads) {
        node[u].push([v, w])
        node[v].push([u, w])
    }

    const bfs = () => {
        const visit = Array(n + 1).fill(0)
        visit[1] = 1
        const q = [1]
        let idx = 0
        let v = Infinity

        while (q.length > idx) {
            const now = q[idx++]

            for (const [nxt, value] of node[now]) {
                v = Math.min(v, value)
                if (!visit[nxt]) {
                    visit[nxt] = 1
                    q.push(nxt)
                }
            }
        }

        return visit[n] ? v : -1
    }

    return bfs()
};