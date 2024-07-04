const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let cnt = 0;
let arr = [];
let result = [];
let N;
rl.on('line', (input) => {
    if (cnt === 0) {
        N = Number(input)
    } else if (cnt <= N) {
        arr.push(Number(input))
    } else {
        result.push(Number(input))
    }
    cnt += 1
})

rl.on('close', () => {
    // console.log(arr)
    // console.log(result)
    const visit = Array(N).fill(false)
    let total = 0;
    let max = 0;

    for (let i = 0; i < N; i++) {
        if (visit[i]) continue;

        let count = 1;
        visit[i] = true
        let [index, next] = [i, arr[i]]
        let flag = 0;
        while (true) {
            const value = result.indexOf(next);
            if (index === value) {
                break
            }

            if (visit[value]) {
                flag = 1
                break;
            }

            [index, next] = [value, arr[value]]
            visit[value] = true;
            count += 1
        }

        if (flag) {
            total += 1
            max = Math.max(max, count);
            // console.log(i, count, visit)
        }

    }

    if (total > 0) {
        console.log(total, max)
    } else {
        console.log(0, -1)
    }
})