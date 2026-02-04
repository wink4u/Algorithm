const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");


function permutation(str, k) {
    const fact = Array(11).fill(1);
    const n = str.length;

    for (let i = 1; i <= 10; i++) fact[i] = fact[i - 1] * i;
    if (k > fact[n]) return 'No permutation';

    k -= 1;
    const res = [];

    for (let size = n; size >= 1; size--) {
        const block = fact[size - 1];
        const idx = Math.floor(k / block);
        res.push(str[idx]);
        str.splice(idx, 1);
        k %= block;
    }
    return res.join("");
}

input.forEach((v, _) => {
    const arr = v.split(' ')
    const s = arr[0].split('')
    const k = Number(arr[1])

    console.log(`${arr[0]} ${k} = ${permutation(s, k)}`)
})