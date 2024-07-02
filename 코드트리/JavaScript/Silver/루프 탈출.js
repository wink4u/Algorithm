const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let N;
let arr = [];
let cnt = 0;

rl.on('line', (input) => {
    if (cnt === 0){
        N = parseInt(input)
    } else {
        arr.push(Number(input) - 1)
    }
    cnt += 1
})

rl.on('close', () => {
    // visit의 0은 방문 X
    let res = [];

    for (let pre = 0; pre < N; pre++){
        let check = [];
        let visit = Array(N).fill(0)
        let next = arr[pre];
        let flag = 1;
        // flag => 1은 루프 X 2는 루트 O
        if (next === -1) continue
        if (res.includes(pre)) continue

        visit[pre] = true
        check.push(pre);

        while (true) {
            let value = arr[next];

            if (value === -1){
                break;
            } else {
                if (visit[value] === true){
                    flag = 2;
                    break;
                } else {
                    visit[value] = true
                    next = value
                }
                check.push(value)
            }
        }

        if (flag === 2) {
            for (let j = 0; j < check.length; j++){
                res.push(check[j])
            }
        }
    }

    let answer = N;
    for (let i = 0; i < N; i++){
        if (res.includes(i)){
            answer -= 1
        }
    }

    console.log(answer);
})