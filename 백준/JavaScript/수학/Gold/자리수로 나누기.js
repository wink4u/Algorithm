const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const n = input[0].split('')
    const arr = n.filter((v) => v !== '0').map(Number)
    const checkNum = (num) => {
        for (let i = 0; i < arr.length; i++) {
            if (num % arr[i]) return false
        }
        return true
    }
    

    const check = Number(n.join(''));
    if (checkNum(check)) {
        console.log(check)
        process.exit()
    }

    const prefix = String(n.join(''))
    let plusNum = 0;
    let len = 1;
    
    while (true) {
        const suffix = String(plusNum).padStart(len, '0');
        const transNum = Number(prefix + suffix)
        if (checkNum(transNum)) {
            console.log(transNum)
            break
        }

        plusNum += 1;
        if (plusNum === 10 ** len) {
            len += 1;
            plusNum = 0;
        }
    }

    process.exit();
})
