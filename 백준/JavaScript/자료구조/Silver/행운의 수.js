const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const T = Number(input[0])

let idx = 1

const check = (v) => {
    const value = String(v)

    for (let i = 0; i < value.length; i++){
        if (value[i] === '5' || value[i] === '8') continue
        else return false
    }

    return true
}
for (let i = 0; i < T; i++){
    const a = Number(input[idx++])
    const aArr = new Set(input[idx++].split(' ').map(Number))
    const b = Number(input[idx++])
    const bArr = new Set(input[idx++].split(' ').map(Number))
    const c = Number(input[idx++])
    const cArr = new Set(input[idx++].split(' ').map(Number))

    const ans = new Set()

    for (const av of aArr) {
        for (const bv of bArr) {
            for (const cv of cArr) {

                const v = av + bv + cv 


                if (!ans.has(v) && check(v)) {
                    ans.add(v)
                }
            }
        }
    }

    console.log(ans.size)
}