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
    const A = input[1].split(' ').map(Number);
    const arr = A.map((val, idx) => [val, idx])
                    .sort((a, b) => {
                        if (a[0] !== b[0]) return a[0] - b[0];
                        return a[1] - b[1];
                    })
    
    const P = Array(n);

    for (let i = 0; i < n; i++){
        const idx = arr[i][1];
        P[idx] = i;
    }

    console.log(P.join(' '));
    process.exit();
})
