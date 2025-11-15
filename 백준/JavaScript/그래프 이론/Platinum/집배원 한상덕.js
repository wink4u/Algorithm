const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const village = input.slice(1, N + 1).map((v) => v.trim().split(''))
const height = input.slice(N + 1).map((v) => v.split(' ').map(Number))

const heightSet = new Set()
const villageSet = new Set()

const dx = [-1, 1, 0, 0, -1, -1, 1, 1]
const dy = [0, 0, -1, 1, -1, 1, -1, 1]

let [px, py] = [0, 0]
let villageCnt = 0

for (let i = 0; i < N; i++){
    for (let j = 0; j < N; j++){
        heightSet.add(height[i][j])

        if (village[i][j] === 'P'){
            [px, py] = [i, j]
            villageSet.add(height[i][j])
        } else if (village[i][j] === 'K'){
            villageSet.add(height[i][j])
            villageCnt++
        }
    }
}

const heightList = Array.from(heightSet).sort((a, b) => a - b)
const villageList = Array.from(villageSet).sort((a, b) => a - b)

const bfs = (l, r) => {
    let cnt = 0
    const visit = Array.from(Array(N), () => Array(N).fill(0))
    const q = []
    q.push([px, py])
    visit[px][py] = 1
    let idx = 0;

    if (l > height[px][py] || r < height[px][py]) {
        return false
    }

    while (q.length > idx){
        const [x, y] = q[idx++]

        if (village[x][y] === 'K') {
            cnt++
        }

        for (let d = 0; d < 8; d++){
            const nx = x + dx[d]
            const ny = y + dy[d]

            if (0 <= nx && nx < N && 0 <= ny && ny < N && !visit[nx][ny]){
                if (l <= height[nx][ny] && height[nx][ny] <= r) {
                    q.push([nx, ny])
                    visit[nx][ny] = 1
                }
            }
        }
    }

    return cnt === villageCnt ? true : false
}

let ans = Infinity
const heightMax = Math.max(...heightList)
const villageMax = Math.max(...villageList)
const villageMin = Math.min(...villageList)

for (let i = 0; i < heightList.length; i++){
    const temp = heightList[i]

    if (temp > villageMin) break

    let left = villageMax, right = heightMax
    let ansTemp = Infinity

    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        const res = bfs(temp, mid)

        if (res) {
            ansTemp = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }


    ans = Math.min(ans, ansTemp - temp)
}

console.log(ans)