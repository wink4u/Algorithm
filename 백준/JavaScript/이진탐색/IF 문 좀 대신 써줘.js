const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let cnt = 0;
let [N, M] = [0, 0];
const check = [];
const arr = [];

rl.on("line", function (line) {
    if (cnt === 0) {
        [N, M] = line.split(' ').map(Number);
    } else {
        if (cnt <= N) {
            check.push(line.split(' '));  // [칭호, 전투력 상한값]
        } else {
            arr.push(Number(line));  // 캐릭터 전투력
        }
    }
    cnt++;
}).on("close", function () {
    const results = [];

    for (let i = 0; i < M; i++) {
        const value = arr[i];
        let [L, R] = [0, check.length - 1];
        
        while (L <= R) {
            const mid = Math.floor((L + R) / 2);
            if (Number(check[mid][1]) >= value) {
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }

        results.push(check[L][0]);
    }

    console.log(results.join("\n"));
    process.exit();
});
