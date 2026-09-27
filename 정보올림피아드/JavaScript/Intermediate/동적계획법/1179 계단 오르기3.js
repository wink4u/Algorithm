const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const MOD = 1000000007

if (N === 1) {
    console.log(1);
} else {
    const one = new Array(N + 1).fill(0)
    const two = new Array(N + 1).fill(0)

    one[2] = 1;

    for (let i = 3; i <= N; i++){
        one[i] = (one[i - 2] + two[i - 2]) % MOD

        if (i === 3) one[i] = 1

        two[i] = one[i - 1]
    }

    console.log((one[N] + two[N]) % MOD)
}