const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const n = Number(input[0])
let idx = 1

function isBetter(a, b) {
    if (a.sum !== b.sum) return a.sum > b.sum;

    const lenA = a.end - a.start
    const lenB = b.end - b.start

    if (lenA !== lenB) return lenA < lenB

    return a.start < b.start;
}

let total = 0;
const answer = [];

for (let i = 0; i < n; i++){
    const L = Number(input[idx++])
    const arr = input[idx++].split(' ').map(Number)

    let best = {
        sum: arr[0],
        start: 0,
        end: 0,
    }

    let sum = arr[0]
    let start = 0

    for (let j = 1; j < L; j++){
        if (sum <= 0) {
            sum = arr[j]
            start = j
        } else {
            sum += arr[j]
        }

        const current = {
            sum: sum,
            start: start,
            end: j
        }

        if (isBetter(current, best)) {
            best = current
        }
    }

    total += best.sum
    answer.push(`${best.start + 1} ${best.end + 1}`)
}

console.log(total)
console.log(answer.join('\n'))