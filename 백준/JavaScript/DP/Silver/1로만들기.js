const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let N;

rl.on('line', function(line){
    N = Number(line)
}).on('close', function(){
    let res = Infinity;
    let res_arr;

    const dfs = (num, arr, cnt) => {
        if (num === 1 && cnt < res){
            res = cnt;
            res_arr = [...arr];
            return
        }

        if (cnt > res) return

        if (num % 3 === 0){
            const tmp = num / 3;
            arr.push(tmp);
            dfs(tmp, arr, cnt + 1)
            arr.pop();
        } 
        if (num % 2 === 0){
            const tmp = num / 2;
            arr.push(tmp);
            dfs(tmp, arr, cnt + 1)
            arr.pop();
        } 

        const tmp = num - 1;
        arr.push(tmp);
        dfs(tmp, arr, cnt + 1);
        arr.pop()
        
    }

    dfs(N, [N], 0);
    const ans = res_arr.join(' ')

    console.log(res)
    console.log(ans);
    process.exit();
})