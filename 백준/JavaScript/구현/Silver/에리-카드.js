const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K] = input[0].split(' ').map(Number)
const common = input[1].split(' ').map(Number)
const cards = new Set(input[2].split(' ').map(Number))

for (let k = 0; k < K; k++){
    let max = -Infinity
    let check = 0

    for (const c of common){
        for (const card of cards){
            if (max <= c * card) {
                max = c * card
                check = card
            }
        }
    }

    cards.delete(check)
}

let ans = -Infinity

for (const c of common){
    for (const card of cards) {
        ans = Math.max(ans, card * c)
    }
}

console.log(ans)
