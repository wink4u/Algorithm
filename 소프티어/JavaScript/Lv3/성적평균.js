const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];
rl.on('line', function(line){
    input.push(line.split(' ').map((i, _) => Number(i)))
}).on('close', function() {
    const [N, K] = input[0];
    const score = input[1];
    const arr = input.slice(2);

    const sum_arr = [0];

    for (let i = 0; i < N; i++){
        sum_arr.push(sum_arr[i] + score[i])
    }

    for (let i = 0; i < K; i++){
        const [s, e] = arr[i];
        let total = sum_arr[e] - sum_arr[s - 1]
        total /= e - s + 1
        const tmp = total.toFixed(2);

        console.log(tmp)
    }
})