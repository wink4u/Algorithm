const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    let N = Number(input[0])
    const primeNum = [];

    const check = () => {
        const v = Array(N).fill(0)

        for (let i = 2; i <= N; i++){
            if (v[i] === 1) continue

            primeNum.push(i)
            for (let j = i; j <= N; j += i){
                v[j] = 1
            }
        }
    }

    check()

    let [left, right] = [0, 0]
    let value = 0;
    let ans = 0;

    while (left <= right) {
        if (value >= N) {
            if (value === N) {
                ans += 1
            }

            value -= primeNum[left]
            left += 1
        } else {
            value += primeNum[right]
            right += 1
            if (right > primeNum.length) break;
        }

    }

    console.log(ans)
    process.exit();
})
