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
    const N = Number(input.shift())
    const ans = [];

    const check = (str) => {
        while (str.length > 1 && str[0] == '0') {
            str = str.substring(1, )
        }
        ans.push(str)
    }

    for (let i = 0; i < N; i++){
        const s = input[i]
        let tmp = ''

        for (let j = 0; j < s.length; j++){
            if (isNaN(s[j]) === false) tmp += s[j]
            else {
                if (tmp !== ''){
                    check(tmp)
                    tmp = ''
                }
            }
        }

        if (tmp !== ''){
            check(tmp)
            tmp = ''
        }

    }
    

    ans.sort((a, b) => a - b);

    for (let i = 0; i < ans.length; i++){
        console.log(ans[i])
    }

})