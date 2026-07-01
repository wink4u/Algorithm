/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumSafenessFactor = function(grid) {
    const n = grid.length;

    if (grid[0][0] === 1 || grid[n-1][n-1] === 1) return 0;

    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const safeness = Array.from(Array(n), () => Array(n).fill(-1));
    let q = [];
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                q.push([i, j]);
                safeness[i][j] = 0;
            }
        }
    }

    let head = 0;
    while (head < q.length) {
        const [x, y] = q[head++];
        for (let d = 0; d < 4; d++) {
            const nx = x + dx[d];
            const ny = y + dy[d];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && safeness[nx][ny] === -1) {
                safeness[nx][ny] = safeness[x][y] + 1;
                q.push([nx, ny]);
            }
        }
    }

    const canReachWithSafeness = (X) => {
        if (safeness[0][0] < X) return false;

        const visit = Array.from(Array(n), () => Array(n).fill(false));
        const bfsQ = [[0, 0]];
        visit[0][0] = true;

        let bHead = 0;
        while (bHead < bfsQ.length) {
            const [x, y] = bfsQ[bHead++];

            if (x === n - 1 && y === n - 1) return true;

            for (let d = 0; d < 4; d++) {
                const nx = x + dx[d];
                const ny = y + dy[d];

                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visit[nx][ny]) {
                    if (safeness[nx][ny] >= X) {
                        visit[nx][ny] = true;
                        bfsQ.push([nx, ny]);
                    }
                }
            }
        }
        return false;
    };

    let left = 0;
    let right = 2 * n; 
    let ans = 0;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (canReachWithSafeness(mid)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return ans;
};