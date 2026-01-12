const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.trim())

const title = []
const problem = []

for (let i = 0; i < N; i++){
    const test = arr[i].split('/')
    
    if (test[0] === 'boj.kr') problem.push(Number(test[1]))
    else title.push(arr[i])
}

title.sort((a, b) => {
    if (a.length !== b.length) {
        return a.length - b.length
    } else {
        for (let i = 0; i < a.length; i++){
            if (a[i] !== b[i]) {
                return a[i] < b[i] ? -1 : 1
            }
        }
    }
})

problem.sort((a, b) => a - b)

if (title.length) console.log(title.join('\n'))
console.log(problem.map(v => 'boj.kr/' + String(v)).join('\n'))