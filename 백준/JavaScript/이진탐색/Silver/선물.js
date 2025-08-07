const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input =[];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const [N, L, W, H] = input[0].split(' ').map(Number);
    function check(a) {
        return Math.floor(L / a) * Math.floor(W / a) * Math.floor(H / a) >= N;
    }

    let [left, right] = [0, Math.max(L, Math.max(W, H))]
    let ans = 0;

    for (let i = 0; i < 100; i++) {
        const mid = (left + right) / 2;
        if (check(mid)) {
            ans = mid;
            left = mid;
        } else {
            right = mid;
        }
    }

    console.log(ans.toFixed(9));
    process.exit();
})
