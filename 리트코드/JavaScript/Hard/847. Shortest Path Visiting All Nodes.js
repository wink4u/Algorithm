/**
 * @param {number[][]} graph
 * @return {number}
 */
var shortestPathLength = function(graph) {
    const n = graph.length
    let ans = (1 << n) + 1

    const visit = Array.from(Array(n), () => Array(1 << n).fill(false))
    const q = []
    let idx = 0

    for (let i = 0; i < n; i++){
        const initState = 1 << i
        visit[i][initState] = true
        q.push([i, initState, 0])
    }


    while (q.length > idx) {
        const [now, state, distance] = q[idx++]

        if (state === (1 << n) - 1) return distance

        for (const nxt of graph[now]) {
            const nxtState = state | (1 << nxt)

            if (!visit[nxt][nxtState]) {
                visit[nxt][nxtState] = true
                q.push([nxt, nxtState, distance + 1])
            }
        }
    }



    return 0
};