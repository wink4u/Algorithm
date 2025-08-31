const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const N = Number(input.shift())
    const set = new Set(input[0].split(' ').map(Number))
    const arr = Array.from(set).sort((a, b) => a - b)
    console.log(arr.join(' '))
    process.exit()
})
