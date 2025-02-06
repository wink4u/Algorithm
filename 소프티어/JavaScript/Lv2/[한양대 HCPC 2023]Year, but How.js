
const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let arr = [];

rl.on('line', (input) => {
    arr = input.split("")
})

rl.on('close', () => {
    let ans = [];
    
    let stack = [];

    arr.forEach((s) => {
        if (s === '(') {
            ans.push(s)
        } else {
            ans.push('1')
            ans.push(s)
            ans.push('+')
        }
    })
    ans.pop()
    const tmp = ans.join('')
    
    console.log(tmp)
})