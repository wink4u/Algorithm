const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => Number(v))

const set = new Set(arr)

const check = (num) => {
    const isVisit = new Set()

    isVisit.add(num)

    const q = [num]
    let range = 1;

    while (q.length) {
        const k = q.length

        for (let i = 0; i < k; i++) {
            const cur = q.shift()

            for (let next = cur - range; next <= cur + range; next++) {
                if (set.has(next) && !isVisit.has(next)) {
                    isVisit.add(next)
                    q.push(next)
                }
            }
        }
        range++
    }

    return isVisit.size
}

let ans = 1;

for (const num of arr) {
    ans = Math.max(ans, check(num))
}

console.log(ans)

