const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input;

rl.on('line', function(line){
    input = line.split(' ').map(Number)
}).on('close', function() {
    let K = BigInt(input[0])
    const P = BigInt(input[1])
    const N = BigInt(input[2] * 10)

    // console.log(K, P, N)

    const check = (x, y) => {
        if (y === BigInt(1)){
            return BigInt(x)
        } else if (y % BigInt(2) === BigInt(1)){
            const res = check(x, (y - BigInt(1)) / BigInt(2))
            return res * res * x % BigInt(1000000007)
        } else{
            const res = check(x, y / BigInt(2))
            return res * res % BigInt(1000000007)
        }
    }

    ans = check(P, N) * K
    ans %= BigInt(1000000007)

    console.log(Number(ans))
})