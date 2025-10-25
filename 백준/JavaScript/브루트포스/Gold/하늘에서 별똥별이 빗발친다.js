const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const [N, M, L, K] = input[0].split(' ').map(Number)
const stars = input.slice(1).map((v) => v.split(' ').map(Number))

let max = 0;

for (let i = 0; i < K; i++) {
    for (let j = 0; j < K; j++) {
        const [x1, tt] = stars[i];
        const [ts, y1] = stars[j];

        let cnt = 0;
        for (let k = 0; k < K; k++) {
            const [x, y] = stars[k];
            if (x1 <= x && x <= x1 + L && y1 <= y && y <= y1 + L) {
                cnt++;
            }
        }

        max = Math.max(max, cnt);
    }
}

console.log(K - max);