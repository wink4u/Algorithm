const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const shape = input.slice(0, 9).map(v => v.trim().split(' '))
const n = Number(input[9])
const arr = input.slice(10).map(v => v.trim().split(' '))
const ans = {}
let num = 0

for (let i = 0; i < 7; i++){
    for (let j = i + 1; j < 8; j++){
        for (let k = j + 1; k < 9; k++){
            const [a, b, c] = [shape[i], shape[j], shape[k]]
            let cnt = 0
            
            for (let idx = 0; idx < 3; idx++){
                if ((a[idx] === b[idx] && a[idx] === c[idx] && b[idx] === c[idx]) ||
                        (a[idx] !== b[idx] && b[idx] !== c[idx] && a[idx] !== c[idx])){
                    cnt++
                } else {
                    break
                }

            }

            if (cnt === 3) ans[`${i + 1}${j + 1}${k + 1}`] = true, num++

        }
    }
}

const check = new Set()
let res = 0
let flag = 0

for (let i = 0; i < n; i++){
    if (arr[i][0] === 'H'){
        const v = arr[i].slice(1).sort().join('')

        if (ans[v] && !check.has(v)) {
            res++
            check.add(v)
        } else {
            res--
        }
    } else {
        if (!flag) {
            if (check.size === num) {
                res += 3
                flag = 1
            } else {
                res--
            }
        } else {
            res -= 1
        }
    }
}

console.log(res)