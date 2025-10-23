const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const n = Number(input[0])
const arr = input[1].split(' ').map(Number)
const stack = []
const ans = Array(n).fill(0)

for (let i = 0; i < n; i++){
    let now = stack.length
    while (now){
        if (stack[now - 1][1] > arr[i]){
            ans[i] = stack[now - 1][0]
            break
        }

        now--
        stack.pop()
    }

    stack.push([i + 1, arr[i]])
}

console.log(ans.join(' '))