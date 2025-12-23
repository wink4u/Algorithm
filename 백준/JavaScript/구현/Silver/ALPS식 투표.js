const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const X = Number(input[0])
const N = Number(input[1])

const people = input.slice(2).map((v) => v.trim().split(' ')).map(([name, value]) => [name, Number(value)])
const check = {}
const ans = []
let idx = 0

for (let i = 0; i < N; i++){
    const [name, value] = people[i]

    if (value * 20>= X) {
        check[name] = [idx, value]
        ans.push([name, 0])
        idx++
    }
}


const tmp = []

for (let i = 1; i <= 14; i++){
    // let v = 0
    Object.values(check).forEach((value) => {
        const [idx, v] = value
        tmp.push([v / i, idx])
    })
}

tmp.sort((a, b) => b[0] - a[0]);

for (let i = 0; i < 14; i++) {
    ans[tmp[i][1]][1] += 1 
}


ans.sort((a, b) => a[0].localeCompare(b[0]));

console.log(ans.map((v) => v.join(' ')).join('\n'))