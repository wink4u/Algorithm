const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const prefix = 'a'.repeat(N - 2)

console.log(prefix + 'FB')
console.log(prefix + 'Ea')
