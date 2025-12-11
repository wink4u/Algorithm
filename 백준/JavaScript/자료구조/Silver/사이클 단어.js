const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])

const check = {}
let cnt = 0

for (let i = 1; i <= N; i++){
    const s = input[i].trim().split('')
    let flag = 0


    for (let j = 0; j <= s.length; j++){
        const tmp = s.shift()
        s.push(tmp)

        const k = s.join('')

        if (check[k]) {
            flag = 1
            break
        }
    }

    if (!flag) {
        check[s.join('')] = true
        cnt++
    }
}

console.log(cnt)