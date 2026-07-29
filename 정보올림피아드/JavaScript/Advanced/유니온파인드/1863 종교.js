const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number)
const friends = input.slice(1).map(v => v.split(' ').map(Number))
const parent = new Array(N + 1).fill(0).map((_ , i) => i)

function find (x) {
    if (x === parent[x]) return x

    parent[x] = find(parent[x])
    return parent[x]
}

const check = new Set()

function union (a, b) {
    const pa = find(a)
    const pb = find(b)

    if (pa === pb) return false

    if (pa < pb) {
        parent[pb] = pa
    } else {
        parent[pa] = pb
    }

    return true
}

let ans = N

for (const [a, b] of friends){
    if (union(a, b)) ans--
}

console.log(ans)