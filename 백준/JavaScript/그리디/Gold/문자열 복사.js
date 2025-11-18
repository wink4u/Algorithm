const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const s = input[0].trim()
const p = input[1].trim()

let index = 0
let ans = 0

while (index < p.length) {
    let tmp = 0, cnt = 0, sIdx = 0

    while ((sIdx < s.length) && index + tmp < p.length) {
        if (p[index + tmp] === s[sIdx]){
            tmp++
            cnt = Math.max(cnt, tmp)
        } else {
            tmp = 0
        }
        sIdx++
    }

    index += cnt
    ans++
}

console.log(ans)