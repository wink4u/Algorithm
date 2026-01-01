const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const check = input[1].split(' ').map(Number)

const arr = input.slice(2).map(v => v.split(' ').map(Number))
let min = Infinity
let ans = []

const dfs = (cost, idx, a, b, c, d, res) => {
    if (cost > min) {
        return
    }


    if (a >= check[0] && b >= check[1] && c >= check[2] && d >= check[3]) {
        if (cost < min) {
            min = cost
            ans = [[...res]]
        } else if (cost === min) {
            ans.push([...res])
        }

        return
    }

    for (let i = idx; i < N; i++){
        res.push(i + 1)
        dfs(cost + arr[i][4], i + 1, a + arr[i][0], b + arr[i][1], c + arr[i][2], d + arr[i][3], res)
        res.pop()
    }
}

dfs(0, 0, 0, 0, 0, 0, [])

if (ans.length === 0) {
    console.log(-1)
} else {

    console.log(min)
    
    ans.sort((a, b) => {
        const len = Math.min(a.length, b.length)
        for (let i = 0; i < len; i++) {
            if (a[i] !== b[i]) return a[i] - b[i]
        }
        return a.length - b.length
    })
    
    console.log(ans[0].join(' '))
}