const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const n = Number(input[0])
const locate = [0, 0, 0, 0]
for (let i = 1; i <= n; i++){
    const c = input[i].trim()
    if (c === 'KBS1') {
        locate[0] = i - 1
        locate[1] = i - 1
    } else if (c === 'KBS2') {
        locate[2] = i - 1
        locate[3] = i - 2
    }
}

if (locate[0] > locate[2]) {
    locate[2] += 1
    locate[3] += 1
}

const ans = [];
for (let i = 0; i < 4; i++){
    if (i % 2){
        ans.push('4'.repeat(locate[i]))
    } else {
        ans.push('1'.repeat(locate[i]))
    }
}

console.log(ans.join(''))