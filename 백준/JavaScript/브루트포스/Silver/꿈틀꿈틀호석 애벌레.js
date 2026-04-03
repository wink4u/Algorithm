const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

let left = 0, right = 0
let total = 0
let ans = 0

const check = []

while (left <= right && right < N){
    if (total < K){
        total += arr[right]
        right += 1 
    } else {
        total -= arr[left]
        left += 1
    }


    if (total >= K) check.push([left, right, total])
}


const dfs = (idx, prevRight, v) => {
    ans = Math.max(ans, v)
    
    for (let i = idx; i < check.length; i++){
        const [left, right, total] = check[i]

        if (prevRight <= left) {
            v += total - K
            dfs(idx + 1, right, v)
            v -= total - K
        }
    }
}

dfs(0, 0, 0)

console.log(ans)