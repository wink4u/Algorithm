const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
    const [N, K] = input.shift().split(" ").map(Number);
    const A = input[0].split(" ").map(BigInt);
    const B = input[1].split(" ").map(BigInt);

    A.sort((a, b) => (a < b ? -1 : 1));
    B.sort((a, b) => (a < b ? -1 : 1));

    const countPairs = (mid) => {
        let cnt = 0n;
        let j = BigInt(N - 1);

        for (let i = 0; i < N; i++) {
            while (j >= 0 && A[i] * B[Number(j)] > mid) {
                j--;
            }
            cnt += (j + 1n);
        }
        return cnt;
    };

    let start = A[0] * B[0];
    let end = A[N - 1] * B[N - 1];
    let answer = 0n;
    const Kbig = BigInt(K);

    while (start <= end) {
        const mid = (start + end) / 2n;
        const cnt = countPairs(mid);

        if (cnt < Kbig) {
            start = mid + 1n;
        } else {
            answer = mid;
            end = mid - 1n;
        }
    }

    console.log(answer.toString());
});
