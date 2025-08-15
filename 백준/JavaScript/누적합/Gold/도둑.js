const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const T = Number(input[0])

    for (let i = 0; i < T; i++) {
        const [N, M, K] = input[(i * 2) + 1].split(' ').map(Number)
        const arr = input[(i * 2) + 2].split(' ').map(Number)

        if (N === M) {
            const sum = arr.reduce((a, b) => a + b);
            const res = sum < K ? 1 : 0
            console.log(res)
            continue
        }

        const arr2 = arr.concat(arr.slice(0, M - 1))
        const tmp = Array(N + M).fill(0)
        
        for (let j = 0; j < N + M - 1; j++) {
            tmp[j + 1] = tmp[j] + arr2[j]
        }

        let cnt = 0;

        for (let k = M; k < N + M; k++){
            if (tmp[k] - tmp[k - M] < K) cnt++
        }

        console.log(cnt)
    }
    process.exit();
})
