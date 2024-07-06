const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let arr =[];
let ans = 3000001

rl.on('line', (input) => {
    arr.push(Number(input))
})

rl.on('close', () => {
    const teams = Array.from({length : 4}, () => []);
    const dfs = (idx) => {
        if (idx === 12) {
            let teamSums = teams.map(team => team.reduce((sum, member) => sum + member, 0))
            let maxSum = Math.max(...teamSums);
            let minSum = Math.min(...teamSums);
            let diff = maxSum -minSum

            if (diff < ans) ans = diff
            return
        }

        for (let i = 0; i < 4; i++){
            if (teams[i].length < 3){
                teams[i].push(arr[idx])
                dfs(idx + 1);
                teams[i].pop();
            }
        }
    }

    dfs(0)
    console.log(ans);
})