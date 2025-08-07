const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const n = Number(input[0]); 
    const arr = input.slice(1, 1 + n).map(Number);
    
    const res = Array(n);
    let check =  arr[0];
    for (let i = 1; i < n; i++){
        if (i % 2) {
            check -= arr[i]
        } else {
            check += arr[i]
        }
    }
    
    
    res[0] = Math.floor(check / 2);
    let idx = 1;
    console.log(res[0])
    for (let i = 0; i < n - 1; i++){
        res[idx] = arr[i] - res[idx - 1];
        console.log(res[idx])
        idx += 1
    }

    
    process.exit();
})
