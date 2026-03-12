const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))

const v = []
const small = []
const big = []

for (let i = 0; i < N; i++){
    const [a, b] = arr[i]
    small.push(a - b)
    big.push(a + b)
    v.push([a - b, a + b])
}

small.sort((a, b) => a - b)
big.sort((a, b) => a - b)

const binary = (v, flag) => {
    let left = 0, right = N

    // flag가 0일때 lower, 1일때 upper

    while (left < right) {
        const mid = Math.floor((left + right) / 2)

        if (!flag) {
            if (big[mid] < v) {
                left = mid + 1
            } else {
                right = mid
            }
        } else {
            if (small[mid] <= v) {
                left = mid + 1
            } else {
                right = mid
            }
        }
    }

    return right
}

const ans = []
for (let i = 0; i < N; i++){
    const left = binary(v[i][0], 0)
    const right = binary(v[i][1], 1)

    ans.push([left + 1, right])
}

console.log(ans.map(v => v.join(' ')).join('\n'))

