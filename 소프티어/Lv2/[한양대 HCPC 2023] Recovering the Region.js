const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let arr = [];
let n;
let cnt = 0;
rl.on('line', (input) => {
    if (cnt === 0) n = Number(input)
    else{
        arr.push(input.split(' ').map(Number))
    }
    cnt += 1
})

rl.on('close', () => {
    for (let i = 1; i < n + 1; i++){
        const visit = Array(n).fill(i)
        console.log(visit.join(' '))
    }

})