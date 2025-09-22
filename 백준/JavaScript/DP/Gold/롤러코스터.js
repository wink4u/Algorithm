const { Console } = require('console');
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
    const arr = input[0].split(' ').map(Number)
    const dp = Array(N).fill(1)
    const rdp = Array(N).fill(1)

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < i; j++) {
            if (arr[j] > arr[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }

    for (let i = N - 1; i >= 0; i--) {
        for (let j = N - 1; j > i; j--) {
            if (arr[j] > arr[i]) {
                rdp[i] = Math.max(rdp[i], rdp[j] + 1);
            }
        }
    }

    let ans = 0;
    
    for (let i = 0; i < N; i++) {
        ans = Math.max(ans, dp[i] + rdp[i] - 1);
    }

    console.log(ans);

})