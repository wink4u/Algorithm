const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    let n = Number(input[0]) + 1
    let ans = ''
    while (n > 1) {
        ans = (n % 2 ? '7' : '4') + ans
        n = Math.floor(n / 2);
    }

    console.log(ans)
    process.exit();
})
