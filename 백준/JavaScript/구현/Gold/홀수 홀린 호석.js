const { Console } = require('console');
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const n = input.shift().split('').map(Number)
    let [min, max] = [Infinity, 0]

    const numCheck = (arr) => {
        let v = 0
        arr.forEach((value) => {
            if (value % 2 === 1) v += 1
        })
        return v
    }

    const dfs = (arr, v) => {
        v += numCheck(arr)
        if (arr.length === 1) {
            min = Math.min(min, v)
            max = Math.max(max, v)
            return
        } else if (arr.length === 2) {
            dfs(String(Number(arr[0]) + Number(arr[1])).split(''), v)
        } else {
            for (let i = 1; i <= arr.length - 2; i++){
                for (let j = i + 1; j <= arr.length - 1; j++){
                    const left = Number(arr.slice(0, i).join(''))
                    const mid = Number(arr.slice(i, j).join(''))
                    const right = Number(arr.slice(j).join(''))
                    
                    const sum = String(left + mid + right).split('')
                    dfs(sum, v)
                }
            }
        }
    }

    dfs(n, 0)
    console.log(min, max)
})