const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const N = Number(input[0])
const weight = input[1].split(' ').map(Number)
const M = Number(input[2])
const check = input[3].split(' ').map(Number)

const stack = []
const DP = Array(40001).fill(0)
DP[weight[0]] = 1
stack.push(weight[0])

for (let i = 1; i < N; i++){
    const now = weight[i]
    const len = stack.length

    for (let j = 0; j < len; j++){
        const minus = Math.abs(stack[j] - now)
        const plus = stack[j] + now

        if (!DP[minus]) {
            DP[minus] = 1
            stack.push(minus)
        }

        if (!DP[plus]) {
            DP[plus] = 1
            stack.push(plus)
        }
    }

    if (!DP[now]){
        DP[now] = 1
        stack.push(now)
    }
}

const ans = []
check.map(v => DP[v] ? ans.push('Y') : ans.push('N'))
console.log(ans.join(' '))