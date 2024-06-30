const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const cal = (arr1, arr2) => {
    for (let i = 0; i < 9; i++){
        if (arr1[i] + arr2[i] >= 10) return false
    }

    return true
}

let res = 0;

const backTracking = (idx, cnt, total) => {
    if (res < cnt){
        // console.log(cnt, total)
        res = cnt
    }

    for (let i = idx; i < N; i++) {
        if (cal(arr[i], total)){
            let value = total.slice();

            for (let j = 0; j < 9; j++) {
                value[j] += arr[i][j]
            }

            backTracking(i + 1, cnt + 1, value)
        }
    }
}


let cnt = 0;
let N = 0;
let arr = [];

rl.on("line", (input) => {
    if (cnt === 0) {
        N = input
    } else {
        const tmp = Array(9).fill(0);
        const num = input.toString();

        for (let i = 0; i < num.length; i++){
            tmp[i] = parseInt(num[num.length - 1 - i])
        }

        arr.push(tmp)
    }
    cnt += 1
})

rl.on("close", () => {
    const check = Array(9).fill(0);
    backTracking(0, 0, check)
    console.log(res)

})
