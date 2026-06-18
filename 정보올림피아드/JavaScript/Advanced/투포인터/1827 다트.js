const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number)
const scores = input.slice(1).map(Number).sort((a, b) => a - b)

const arr = [0]

for (let i = 0; i < N; i++){
    if (scores[i] <= M) arr.push(scores[i])
}

for (let i = 0; i < N; i++){
    for (let j = 0; j < N; j++){
        if (scores[i] + scores[j] <= M) arr.push(scores[i] + scores[j])
    }
}

arr.sort((a, b) => a - b)

let ans = 0
let left = 0
let right = arr.length - 1

while (left <= right) {
    const v = arr[left] + arr[right]

    if (v <= M) {
        ans = Math.max(ans, v)
        left++
    } else {
        right--
    }
}

console.log(ans)