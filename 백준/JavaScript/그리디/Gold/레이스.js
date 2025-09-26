const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
    const [N, M, K] = input.shift().split(' ').map(Number)
    const arr = input[0].split(' ').map(Number)

    let [left, right] = [0, arr[K - 1] - arr[0]]
    let check = 0;

    while (left <= right){
        const mid = Math.floor((left + right) / 2)
        let cnt = 1;
        let prev = arr[0]
        for (let i = 1; i < K; i++){
            if (arr[i] - prev >= mid){
                cnt += 1;
                prev = arr[i]
            }
        }

        if (cnt < M) {
            right = mid - 1
        } else {
            check = mid
            left = mid + 1
        }
    }

    const answer = ['1']
    let refree = 1
    let checkRefree = arr[0]

    for (let i = 1; i < K; i++){
        if (arr[i] - checkRefree >= check && refree < M) {
            refree += 1
            answer.push('1')
            checkRefree = arr[i]
        } else {
            answer.push('0')
        }
    }

    console.log(answer.join(''))

});
