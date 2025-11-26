const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

const min = Math.min(...arr)
let [left, right] = [1, min * M]

const check = (value) => {
    let cnt = 0

    for (let i = 0; i < N; i++){
        cnt += Math.floor(value / arr[i])
    
        if (cnt >= M) return true
    }

    return false
}

let ans = 0

while (left <= right) {
    const mid = Math.floor((left + right) / 2)

    if (check(mid)){
        right = mid - 1
        ans = mid
    } else {
        left = mid + 1
    }
}

console.log(ans)