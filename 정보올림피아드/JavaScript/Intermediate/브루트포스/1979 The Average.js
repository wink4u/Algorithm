const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [N1, N2, N] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

arr.sort((a, b) => a - b)
const ans = Math.floor((arr.slice(N2, N - N1).reduce((a, b) => a + b, 0)) / (N - N1 - N2))

console.log(ans)