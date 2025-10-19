const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const left = input[0].trim().split('');
const right = [];
const M = Number(input[1])
console.log(left, right)

for (let i = 2; i < M + 2; i++){
    const [cmd, v] = input[i].trim().split(' ')
    if (cmd === 'L' && left.length) right.push(left.pop())
    else if (cmd === 'D' && right.length) left.push(right.pop())
    else if (cmd === 'B' && left.length) left.pop()
    else if (cmd === 'P') left.push(v)
}

console.log(left.join('') + right.reverse().join(''))
