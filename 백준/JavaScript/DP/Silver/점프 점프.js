const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let cnt = 0;
let N ;
let arr = [];

rl.on("line", function (line) {
    if (cnt === 0){
        N = Number(line)
    } else {
        arr = line.split(' ').map(Number)
    }
    cnt++;
}).on("close", function () {
    const DP = Array(N).fill(Infinity);
    DP[0] = 0

    for (let i = 0; i < N; i++){
        const v = arr[i];

        if (DP[i] !== Infinity){
            for (let j = i + 1; j < Math.min(N, i + v + 1); j++){
                DP[j] = Math.min(DP[j], DP[i] + 1)
            }
        }
    }

    const res = DP[N - 1] === Infinity ? -1 : DP[N - 1];

    console.log(res);
    process.exit();
});
