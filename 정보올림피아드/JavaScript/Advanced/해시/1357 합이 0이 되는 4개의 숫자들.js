const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))

const sumA = new Map()

for (let i = 0; i < N; i++){
    for (let j = 0; j < N; j++){
        const v = arr[i][0] + arr[j][1]
        sumA.set(v, (sumA.get(v) || 0) + 1)
    }
}

let ans = 0

for (let i = 0; i < N; i++){
    for (let j = 0; j < N; j++){
        const v = -(arr[i][2] + arr[j][3])

        if (sumA.get(v)) {
            ans += sumA.get(v)
        }
    }
}

console.log(ans)