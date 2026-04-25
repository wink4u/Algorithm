const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, T] = input[0].split(' ').map(Number)
let ans = Infinity

for (let i = 1; i <= N; i++) {
    const [S, I, C] = input[i].split(' ').map(Number)

    if (T > S + (I * (C - 1))) continue

    let now = S
    let cnt = 0

    while (cnt !== C) {
        if (now >= T) {
            ans = Math.min(ans, now - T)
            break
        }

        now += I
        cnt++
    }
}

console.log(ans === Infinity ? -1 : ans)