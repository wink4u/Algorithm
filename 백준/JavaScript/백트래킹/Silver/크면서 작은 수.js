const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const arr = input[0].split('')
    const k = Number(arr.join(''))
    const len = arr.length;
    let ans = Infinity;

    const dfs = (num, visit) => {
        const v = Number(num.join(''))

        if (num.length === len && v > k) {
            ans = Math.min(ans, v)
            return
        }

        for (let i = 0; i < len; i++){
            if (visit[i] === 0) {
                num.push(arr[i])
                visit[i] = 1
                dfs(num, visit)
                visit[i] = 0
                num.pop()
            }
        }
    }

    dfs([], Array(len).fill(0))

    // console.log(ans);
    console.log(ans === Infinity ? 0 : ans );

    process.exit()
})
