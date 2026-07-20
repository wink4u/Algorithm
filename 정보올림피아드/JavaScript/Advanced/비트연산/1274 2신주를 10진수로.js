const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const s = input[0].split('')
let ans = 0

if (s[0] === '0') {
    for (let i = 7; i >= 1; i--) {
        if (s[i] === '1') ans += 2 ** (7 - i)
    }

    console.log(ans)
} else {
    let flag = 1

    for (let i = 7; i >= 1; i--){
        if (s[i] === '0') {
            if (!flag) {
                ans += 2 ** (7 - i)
            }
        } else {
            if (flag) {
                ans += 2 ** (7 - i)
                flag = 0
            }
        }
    }

    if (flag) ans += 2 ** 8

    console.log(-ans)
}