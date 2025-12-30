const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const T = Number(input[0])

for (let i = 1; i <= T; i++){
    const N = Number(input[i])
    const symbol = ['+', '-', ' ']
    const ans = []

    const check = (arr, num) => {
        if (num > N) {
            
            const value = arr.join('')
            .split(/([+-])/)
            .map(v => (v === '+' || v === '-') ? v : Number(v.replaceAll(' ', '')));
            
            let v = value[0]
            let prev
            for (let k = 1; k < value.length; k++){
                const now = value[k]
                
                if (Number.isInteger(Number(now))) {
                    v += prev === '+' ? now : -now
                } else {
                    prev = now
                }
            }
        
            if (v === 0) ans.push([...arr].join(''))
            return
        }

        for (let j = 0; j < 3; j++){
            arr.push(symbol[j])
            arr.push(num)
            check(arr, num + 1)
            arr.pop()
            arr.pop()
        }
    }

    check([1], 2)

    ans.sort()
    console.log(ans.join('\n'))
    console.log('')
}