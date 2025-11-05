const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const T = Number(input[0])
let idx = 1

for (let t = 0; t < T; t++){
    const [N, M] = input[idx++].split(' ').map(Number)
    const books = input.slice(idx, idx + M).map((v) => v.split(' ').map(Number))
    let ans = 0
    idx += M

    books.sort((a, b) => {
        const e1 = a[1]
        const e2 = b[1]

        if (e1 < e2) return -1
        else return 1
    })

    const check = Array(N + 1).fill(true)

    for (const [s, e] of books) {
        let c = 0

        for (let i = s; i < e + 1; i++){
            if (check[i]) {
                c = i
                break
            }
        }

        if (c) {
            check[c] = false
            ans++
        }
    }

    console.log(ans)
}