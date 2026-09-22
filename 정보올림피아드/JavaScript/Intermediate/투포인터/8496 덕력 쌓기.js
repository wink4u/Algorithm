const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number);
const arr = input.slice(1).map(v => Number(v));

let left = 0;
let total = 0;
let ans = Infinity;

for (let right = 0; right < N; right++) {
    total += arr[right];
    while (total >= M) {
        ans = Math.min(ans, right - left + 1);
        total -= arr[left];
        left++;
    }
}

console.log(ans === Infinity ? -1 : ans);