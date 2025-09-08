const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const N = Number(input.shift())
    const words = input.slice(0, N)
    const M = input[N]

    if (M === 0) process.exit()

    const arr = input.slice(N + 1)

    check = {}

    words.forEach((word) => {
        const l = word.length
        const fb = `${word[0]}${word[l - 1]}`
        const mid = word.slice(1, l - 1).split('').sort().join('')
        
        if (l === 1) {
            check[word] = true
        } else {
            if (check[fb]) {
                if (check[fb][mid]) check[fb][mid] += 1
                else check[fb][mid] = 1
            } else {
                check[fb] = {}
                check[fb][mid] = 1
            }
        }
    })

    arr.forEach((v) => {
        if (N === 0) {
            console.log(0)
        } else {
            v = v.split(' ')
            let ans = 0;
    
            for (let i = 0; i < v.length; i++){
                const vl = v[i].length
    
                if (vl === 1 && check[v[i]]) {
                    if (ans === 0) ans = 1
                    continue
                }
    
                const fb = `${v[i][0]}${v[i][vl - 1]}`
                const mid = v[i].slice(1, vl - 1).split('').sort().join('')
    
                const checkFb = check[fb];
                if (checkFb?.[mid]) {
                    ans = ans > 0 ? ans * checkFb[mid] : checkFb[mid];
                }
            }

            console.log(ans)
        }
    })
})
