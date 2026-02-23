const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [h, v] = input[0].split(' ').map(Number)

if (h === 0 || v === 0) {
    console.log(0)
    process.exit()
}

const hArr = input[1].split(' ').map(Number)
const vArr = input[2].split(' ').map(Number)

const x = new Map()
const y = new Map()

for (let i = 0; i < h - 1; i++){
    for (let j = i + 1; j < h; j++){
        const tmp = hArr[j] - hArr[i]
        
        if (!x.has(tmp)) {
            x.set(tmp, 1)
        } else {
            const now = x.get(tmp)
            x.set(tmp, now + 1)
        }
    }
}

for (let i = 0; i < v - 1; i++){
    for (let j = i + 1; j < v; j++){
        const tmp = vArr[j] - vArr[i]
        
        if (!y.has(tmp)) {
            y.set(tmp, 1)
        } else {
            const now = y.get(tmp)
            y.set(tmp, now + 1)
        }
    }
}

let ans = 0

x.forEach((value, key) => {
    if (y.has(key)){
        ans += value * y.get(key)
    }
})
console.log(ans)
