const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input;

rl.on('line', function(line){
    input = line.split(' ').map((i, _) => Number(i))
}).on('close', function(){
    let K = BigInt(input[0])
    const P = BigInt(input[1])
    const N = input[2]

    for (let i = 0; i < N; i++){
        K *= P
        K %= BigInt(1000000007)
    }
    console.log(Number(K));
})