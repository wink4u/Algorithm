const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0]);

for (let i = 1; i <= N; i++) {
    const arr = input[i].trim().split(' ');
    const m = Number(arr[0]);

    let v = 0;
    let count = 0;

    // Boyer-Moore Majority Vote
    for (let j = 1; j <= m; j++) {
        const num = arr[j];

        if (count === 0) {
            v = num;
            count = 1;
        } else if (v === num) {
            count++;
        } else {
            count--;
        }
    }

    // 검증
    let cnt = 0;
    for (let j = 1; j <= m; j++) {
        if (arr[j] === v) cnt++;
    }

    console.log(cnt > m / 2 ? v : "SYJKGW");
}