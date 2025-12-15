const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K] = input[0].split(' ').map(Number)
const arr = []
let v

for (let i = 1; i <= N; i++){
    const [id, g, s, b] = input[i].split(' ').map(Number)
    if (id === K) v = [g, s, b]
    arr.push([g, s, b])
}

let ans = 1;

for (const [g, s, b] of arr) {
    if ((g > v[0]) ||
        (g === v[0] && s > v[1]) ||
        (g === v[0] && s === v[1] && b > v[2])
    ) {
        ans++
    }
}

console.log(ans)