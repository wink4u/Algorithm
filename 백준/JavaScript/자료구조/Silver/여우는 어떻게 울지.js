const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const T = Number(input[0])
let idx = 1
for (let i = 0; i < T; i++){
    const ans = []
    const sound = input[idx++].trim().split(' ')
    const check = {}

    while (true) {
        let tmp = input[idx++]
        if (tmp === 'what does the fox say?') {
            for (let j = 0; j < sound.length; j++){
                if (check[sound[j]]) continue

                ans.push(sound[j])
            }

            console.log(ans.join(' '))
            break
        }
        
        tmp = tmp.trim().split(' ')
        check[tmp[2]] = true

    }
}