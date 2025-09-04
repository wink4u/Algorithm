const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const [N, M] = input.shift().split(' ').map(Number);
    const arr = input.map((v) => v.split('').map(Number))
    let ans = -1

    const check = (checkArr) => {
        const value = Number(checkArr.join(''))
        if (Math.sqrt(value) % 1 === 0) ans = Math.max(ans, value)

    }

    for (let i = 0; i < N; i++){
        for (let j = 0; j < M; j++){
            check([arr[i][j]])
            for (let dx = -N; dx <= N; dx++){
                for (let dy = -M; dy <= M; dy++){
                    if (dx === 0 && dy === 0) continue

                    let x = i, y = j;
                    let v = [arr[i][j]]

                    while (true) {
                        const [nx, ny] = [x + dx, y + dy]
                        if (nx >= N || ny >= M || nx < 0 || ny < 0) break
                        v.push(arr[nx][ny])
                        check(v)
                        check([...v].reverse())
                        x = nx
                        y = ny
                    }
                }
            }
        }
    }
    console.log(ans);
    process.exit()
})
