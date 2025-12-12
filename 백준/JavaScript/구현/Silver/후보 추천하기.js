const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0])
const M = Number(input[1])
const arr = input[2].split(' ').map(Number)

const check = {}

for (let i = 0; i < M; i++){
    if (check[arr[i]]) {
        check[arr[i]][1] += 1
        continue
    } 


    let cnt = 0
    let idx = 0, v = Infinity, d = 0
    for (const [key, value] of Object.entries(check)) {
        const [now, count] = value

        if (v > count) {
            d = key
            idx = now
            v = count
        } else if (v === count){
            if (now < idx){
                d = key
                idx = now
            }
        }
        cnt++
    }

    if (cnt === N) {
        delete check[d]
    } 
    
    check[arr[i]] = [i, 1]


}

const v = Object.entries(check)
const ans = v.map((k) => Number(k[0]))
console.log(ans.sort((a, b) => a - b).join(' '))