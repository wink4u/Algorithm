const fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, M] = input[0].split(' ').map(Number)
const [sx, sy] = input[1].split(' ').map(Number)
const [ex, ey] = input[2].split(' ').map(Number)


const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const board = input.slice(3).map((v) => v.split(' ').map(Number))

const bfs = () => {
    const visit = Array.from(Array(N), () => Array.from(Array(M), () => Array(2).fill(false)))
    visit[sx - 1][sy - 1][0] = true

    const q = [[sx - 1, sy - 1, 0, 0]]
    let idx = 0;

    while (idx < q.length){
      const [x, y, mg, cost] = q[idx++]
  
      if (x === ex - 1 && y === ey - 1) {
        return cost
      }

      for (let d = 0; d < 4; d++){
        const nx = x + dx[d], ny = y + dy[d]

        if (0 <= nx && nx < N && 0 <= ny && ny < M){
          if (visit[nx][ny][mg]) continue;

          if (board[nx][ny] === 1 && mg === 0) {
            visit[nx][ny][1] = true
            q.push([nx, ny, 1, cost + 1])
          } else if (!board[nx][ny]){
            visit[nx][ny][mg] = true
            q.push([nx, ny, mg, cost + 1])
          }
        }
      }
    }
    return -1
  }

  console.log(bfs())