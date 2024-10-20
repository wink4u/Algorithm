const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const n = Number(input[0])
    const arr = input[1].split(' ').map((i, _) => Number(i))
    const DP = Array(n).fill(1);

    for (let i = 1; i < n; i++){
        for (let j = 0; j < i; j++){
            if (arr[j] < arr[i]) DP[i] = Math.max(DP[i], DP[j] + 1)
        }
    }
    console.log(Math.max(...DP));
    process.exit();
})