const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0])
const board = input.slice(1).map((v) => v.split(' ').map(Number))

let MIN = 200, MAX = 0

board.forEach((v) => {
  MIN = Math.min(MIN, v.reduce((a, b) => Math.min(a, b), 201))
  MAX = Math.max(MAX, v.reduce((a, b) => Math.max(a, b), 0))
})

const s = board[0][0], e = board[N - 1][N - 1]
const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const isMove = (x, y) =>{
  if (0 <= x && x < N && 0 <= y && y < N) return true

  return false
}


const check = (mid) => {
  for (let i = MIN; i <= MAX; i++){
    if (i <= s && s <= i + mid && i <= e && e <= i + mid){
      if (bfs(i, i + mid)) return true
    }
  }
  return false
}

const bfs = (a, b) => {
  const visit = Array.from(Array(N), () => Array(N).fill(false))
  visit[0][0] = true
  const q = [[0, 0]]
  let idx = 0

  while (idx < q.length) {
    const [x, y] = q[idx++]

    if (x === N - 1 && y === N - 1) return true

    for (let d = 0; d < 4; d++){
      const [nx, ny] = [x + dx[d], y + dy[d]]

      if (isMove(nx, ny) && !visit[nx][ny]) {
        const v = board[nx][ny]

        if (a <= v && v <= b) {
          visit[nx][ny] = true
          q.push([nx, ny])
        }
      }
    }
  }

  return false
}


let left = 0, right = MAX
let ans = 0

while (left <= right){
  const mid = Math.floor((left + right) / 2)

  if (check(mid)){
    ans = mid
    right = mid - 1
  } else {
    left = mid + 1
  }
}

console.group(ans)