const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const s = input[0].trim()
const t = input[1].trim()

const check = Array(t.length + 1).fill(0)
const idx = {}
for (let i = 0; i < t.length; i++){
    idx[t[i]] = i + 1
}


check[0] = Infinity

for (let i = 0; i < s.length; i++){
    const v = s[i]

    if (idx[v] > 0 && check[idx[v] - 1] > check[idx[v]]){
        check[idx[v]] += 1
    }
}

console.log(check[t.length])