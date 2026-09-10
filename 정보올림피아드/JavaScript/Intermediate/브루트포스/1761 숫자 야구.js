const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const N = Number(input[0])
const arr = input.slice(1).map(v => v.trim().split(' ').map(Number))

const check = (baseball) => {
    for (const [num, strike, ball] of arr) {
        const sNum = String(num).split('').map(Number)
        let st = 0, ba = 0

        for (let i = 0; i < 3; i++){
            if (baseball[i] === sNum[i]) st++
            else if (sNum.includes(baseball[i])) ba++
        }

        if (st !== strike || ba !== ball) return false
    }

    return true
}


let cnt = 0

for (let i = 1; i <= 9; i++){
    for (let j = 1; j <= 9; j++){
        for (let k = 1; k <= 9; k++){
            if (i !== j && j !== k && i !== k) {
                if (check([i, j, k])) cnt++
            }
        }
    }
}

console.log(cnt)