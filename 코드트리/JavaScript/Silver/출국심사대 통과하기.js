const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let cnt = 0;
let N;
let arr = [];

rl.on('line', (input) => {
    if (cnt) arr.push(input.trim().split(' '))
    else N = Number(input)
    cnt += 1
})

rl.on('close', () => {
    arr.sort((a, b) => {
        return a[0] - b[0];
    });

    let end = Number(arr[0][0]) + Number(arr[0][1])
    for (let i = 1; i < N; i++){
        const [s, e] = [Number(arr[i][0]), Number(arr[i][1])];
        if (end > s) end += e
        else end = s + e
    }

    console.log(end)
})
