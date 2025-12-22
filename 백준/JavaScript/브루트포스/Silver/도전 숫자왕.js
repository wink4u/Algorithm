const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input[1].split(' ').map(Number)
const M = arr.reduce((a, b) => a + b, 0)
const check = new Set()

const dfs = (idx, sum) => {
    if (idx === N) {
        if (sum !== 0) check.add(sum)
        return
    }

    dfs(idx + 1, sum + arr[idx])
    dfs(idx + 1, sum)
}

dfs(0, 0)

console.log(M - check.size)