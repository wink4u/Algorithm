const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const level = input[1].split(' ').map(Number)

const problem = input.slice(2).map((v) => v.split(' ').map(Number))
const check = {}

for (const [l, cnt] of problem){
    if (check[l]) check[l].push(cnt)
    else check[l] = [cnt]
}

let ans = 0
let flag = 0

for (let i = 0; i < 5; i++){
    const v = i + 1
    const cnt = level[i]
    if (cnt) {

        if (flag) {
            ans += 60
        } else {
            flag = 1
        }

        const arr = check[v]
        arr.sort((a, b) => a - b)

        let prev = -1

        for (let j = 0; j < cnt; j++){
            ans += arr[j]

            if (prev === -1) {
                prev = arr[j]
                continue    
            }

            ans += arr[j] - prev
            prev = arr[j]
        }
    }
}

console.log(ans)