const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line) {
    input.push(line.split(' ').map(Number))
}).on('close', function(){
    const [n, m] = input[0]
    const board = input.slice(1, n + 1)
    const go = input.slice(n + 1)

    // console.log(board, go);
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const visit = Array.from(Array(n), () => Array(n).fill(false));
    const new_go = go.map(innerArr => innerArr.map(v => v - 1))

    const [sx, sy] = new_go[0];
    visit[sx][sy] = true
    new_go.shift();

    // console.log(visit)
    // console.log(go);
    let ans = 0;
    const dfs = (x, y, arr, v) => {

        if (arr.length === 0){
            ans += 1
            return
        }

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (0 <= nx && nx < n && 0 <= ny && ny < n){
                if (board[nx][ny] === 0 && !v[nx][ny]) {
                    if (nx === arr[0][0] && ny === arr[0][1]){
                        const [tx, ty] = arr[0]
                        arr.shift()
                        v[nx][ny] = true
                        dfs(nx, ny, arr, v)
                        arr.unshift([tx, ty])
                        v[nx][ny] = false
                    } else {
                        if (arr.includes([nx, ny])){
                            continue
                        }

                        v[nx][ny] = true
                        dfs(nx, ny, arr, v)
                        v[nx][ny] = false
                    }
                }
            }
        }
    }

    dfs(sx, sy, new_go, visit)
    console.log(ans)
})