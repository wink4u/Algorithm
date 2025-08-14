const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const [N, K] = input[0].split(' ').map(Number)
    const arr = input
        .slice(1)
        .map(line => line.split(' ').map(Number))
        .sort((a, b) => a[1] - b[1])
        
    let ans = 0;

    let [left, right] = [0, 0]
    let value = 0
    while (left <= right && right < N) {
        if (arr[right][1] - arr[left][1] <= K * 2) {
            value += arr[right][0]
            ans = Math.max(value, ans)
            right += 1
        } else {
            value -= arr[left][0]
            left += 1
        }
    }

    console.log(ans)

    process.exit();
})
