const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const s = input[0].split('')
const N = s.length
const check = Array(N).fill(false);
let count = 0;

s.sort((a, b) => a.charCodeAt() - b.charCodeAt())

const dfs = (depth, str, lastChar) => {
    if (depth === N) {
        count++;
        return;
    }

    for (let i = 0; i < N; i++) {
        if (check[i]) continue;

        if (s[i] === lastChar) continue;

        if (i > 0 && s[i] === s[i - 1] && !check[i - 1]) continue;

        check[i] = true;
        dfs(depth + 1, str + s[i], s[i]); 
        check[i] = false;
    }
};

dfs(0, "", "");

console.log(count);