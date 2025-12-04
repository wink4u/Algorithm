const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])

let cnt = 0

for (let t = 1; t <= N; t++){
    const s = input[t].trim()
    const tmp = []


    for (let i = 0; i < s.length; i++){
        const k = tmp.length
        if (k) {
            if (tmp[k - 1] === s[i]) tmp.pop()
            else tmp.push(s[i])
        } else {
            tmp.push(s[i])
        }
    }

    if (!tmp.length) cnt++
}

console.log(cnt)