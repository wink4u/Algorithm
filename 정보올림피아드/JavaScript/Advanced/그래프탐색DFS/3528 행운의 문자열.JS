const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const s = input[0].trim();

const check = new Map();

for (let i = 0; i < s.length; i++) {
    const c = s[i]
    check.set(c, (check.get(c) || 0) + 1)
}


const dfs = (prev, cnt) => {
    let answer = 0;

    if (cnt === s.length) return 1

    for (const key of check.keys()) {
        if (ket === prev || check.get(key) === 0) continue;

        check.set(key, check.get(key) - 1)
        answer += dfs(key, cnt + 1)
        check.set(key, check.get(key) + 1)
    }

    return answer
}

console.log(dfs('', 0))