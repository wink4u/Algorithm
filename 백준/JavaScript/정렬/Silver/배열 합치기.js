const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number).concat(input[2].split(' ').map(Number))

arr.sort((a, b) => a - b)
console.log(arr.join(' '))