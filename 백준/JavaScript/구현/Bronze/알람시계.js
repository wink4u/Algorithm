const { Console } = require('console');
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const t = input[0].split(':').map(Number)
    const Time = {
        1 : [0, 0],
        2 : [0, 1],
        3 : [0, 2],
        4 : [1, 0],
        5 : [1, 1],
        6 : [1, 2],
        7 : [2, 0],
        8 : [2, 1],
        9 : [2, 2],
        0 : [3, 1],
    }

    let ans = Infinity
    let res = [];

    const dfs = (arr) => {
        if (arr.length === 4) {
            const [h, m] = [arr[0] * 10 + arr[1], arr[2] * 10 + arr[3]]
            if (h % 24 === t[0] && m % 60 === t[1]) {
                let tmp = 0;

                for (let i = 1; i < 4; i++){
                    const [a, b] = [arr[i - 1], arr[i]]
                    const [ax, ay] = Time[a]
                    const [bx, by] = Time[b]
                    tmp += Math.abs(ax - bx) + Math.abs(ay - by)
                }

                if (ans === tmp) {
                    res.push([h, m])
                } else if (ans > tmp) {
                    ans = tmp
                    res = [[h, m]]
                }
            }
            return
        }

        for (let i = 0; i <= 9; i++){
            arr.push(i)
            dfs(arr)
            arr.pop()
        }
    }

    dfs([])

    res.sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        }

        return a[0] - b[0];
    })

    const trans = (res) => {
        const hh = String(res[0][0]).padStart(2, '0')
        const mm = String(res[0][1]).padStart(2, '0')
        return `${hh}:${mm}`
    }

    console.log(trans(res))
})