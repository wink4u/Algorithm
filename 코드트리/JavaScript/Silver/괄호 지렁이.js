const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let arr =[];
let N;
let cnt = 0;
rl.on('line', (input) => {
    if (cnt === 0) N = Number(input)
    else {
        const tmp = input.trim().split('')
        arr.push(tmp);
    }
    cnt += 1
})

rl.on('close', () => {
    let res = 0;

    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]

    const check = (x, y, inArr, outArr, visit) => {
        if (inArr.length === outArr.length) {
            res = Math.max(inArr.length, res)
        }

        for (let d = 0; d < 4; d++){
            const [nx, ny] = [x + dx[d], y + dy[d]]

            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                if (visit[nx][ny] === false) {
                    const now = arr[nx][ny];

                    if (now === '(') {
                        if (outArr.length === 0) {
                            inArr.push(now)
                            visit[nx][ny] = true
                            check(nx, ny, inArr, outArr, visit)
                            visit[nx][ny] = false
                            inArr.pop()
                        }
                    } else {
                        if (inArr.length > outArr.length) {
                            outArr.push(now)
                            visit[nx][ny] = true
                            check(nx, ny, inArr, outArr, visit)
                            outArr.pop()
                            visit[nx][ny] = false
                        }
                    }
                }
            }
        }
    }

    const v = Array.from(Array(N), () => Array(N).fill(false))
    v[0][0] = true

    if (arr[0][0] === '('){
        check(0, 0, ['('], [], v)
    } else{
        check(0, 0, [], [')'], v)
    }
    console.log(res * 2);
})