const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => {
    const [sm, sd, em, ed] = v.split(' ').map(Number)
    return [sm * 100 + sd, em * 100 + ed]
})

arr.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0]
    return a[1] - b[1]
})


let target = 301
let count = 0
let index = 0
let maxEnd = 0

while (target <= 1130) {
    let found = false
    maxEnd = 0

    while (index < N && arr[index][0] <= target) {
        if (arr[index][1] > maxEnd) {
            maxEnd = arr[index][1]
            found = true
        }

        index++
    }

    if (!found) {
        count = 0
        break
    }

    target = maxEnd
    count++
}

console.log(count)