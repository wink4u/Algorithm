const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    let N = Number(input.shift())
    const arr = input[0].split(' ').map(Number)
    
    const check = Array(51).fill(0)
    for (const v of arr) check[v]++;

    let ans = -1;

    for (let k = 0; k <= 50; k++){
        if (check[k] === k) ans = Math.max(ans, k)
    }

    console.log(ans);
    process.exit();
})
