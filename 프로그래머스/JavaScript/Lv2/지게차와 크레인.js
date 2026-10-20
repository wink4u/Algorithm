function solution(storage, requests) {
    const [n, m] = [storage.length, storage[0].length]
    let answer = n * m

    storage = storage.map(v => v.split(''))

    const visit = Array.from(Array(n), () => Array(m).fill(0))
    const out = Array.from(Array(n), () => Array(m).fill(false))
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (i === 0 || i === n - 1 || j === 0 || j === m - 1) out[i][j] = true
        }
    }

    const expose = (sx, sy) => {
        const stack = [[sx, sy]]

        while (stack.length) {
            const [x, y] = stack.pop()

            for (let d = 0; d < 4; d++) {
                const [nx, ny] = [x + dx[d], y + dy[d]]

                if (nx < 0 || nx >= n || ny < 0 || ny >= m || out[nx][ny]) continue

                out[nx][ny] = true
                if (visit[nx][ny]) stack.push([nx, ny])
            }
        }
    }

    const jige = (word) => {
        const arr = []

        for (let x = 0; x < n; x++) {
            for (let y = 0; y < m; y++) {
                if (!visit[x][y] && out[x][y] && storage[x][y] === word) {
                    arr.push([x, y])
                }
            }
        }

        // 한꺼번에 꺼내고 이웃을 외부와 연결시킨다
        for (const [x, y] of arr) {
            visit[x][y] = 1
            answer -= 1
        }
        for (const [x, y] of arr) expose(x, y)
    }

    const crain = (word) => {
        const arr = []

        for (let x = 0; x < n; x++) {
            for (let y = 0; y < m; y++) {
                if (!visit[x][y] && storage[x][y] === word) {
                    visit[x][y] = 1
                    answer -= 1
                    arr.push([x, y])
                }
            }
        }

        
        for (const [x, y] of arr) {
            if (out[x][y]) expose(x, y)
        }
    }

    for (const request of requests) {
        if (request.length === 1) jige(request)
        else crain(request[0])
    }

    return answer
}