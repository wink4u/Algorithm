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

    const gcd = (a, b) => {
        a = Math.abs(a); b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b; b = t;
        }
        return a;
    };

    let g = 0;
    const base = arr[0];
    for (let i = 1; i < N; i++) {
        g = gcd(g, arr[i] - base);
    }

    console.log(Math.abs(g));
})
