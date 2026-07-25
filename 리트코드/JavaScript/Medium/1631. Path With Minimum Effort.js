/**
 * @param {number[][]} heights
 * @return {number}
 */
var minimumEffortPath = function(heights) {
    const r = heights.length
    const c = heights[0].length

    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]

    const isMove = (x, y) => {return 0 <= x && x < r && 0 <= y && y < c}

    const checkBfs = (v) => {
        const visit = Array.from(Array(r), () => Array(c).fill(0))
        visit[0][0] = 1

        const q = [[0, 0]]
        let idx = 0

        while (q.length > idx) {
            const [x, y] = q[idx++]

            if (x === r - 1 && y === c - 1) return true

            for (let d = 0; d < 4; d++){
                const [nx, ny] = [x + dx[d], y + dy[d]]

                if (isMove(nx, ny)) {
                    const diff = Math.abs(heights[x][y] - heights[nx][ny])

                    if (!visit[nx][ny] && diff <= v) {
                        visit[nx][ny] = 1
                        q.push([nx, ny])
                    }
                }
            }
        }

        return false
    }
    
    let ans = 0

    let left = 0, right = 1000000
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)

        if (checkBfs(mid)) {
            ans = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }

    return ans
};