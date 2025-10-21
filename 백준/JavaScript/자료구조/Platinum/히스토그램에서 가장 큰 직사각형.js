const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

let idx = 0;
const ans = [];

while (true) {
    const block = input[idx++].split(' ').map(Number)
    if (block[0] === 0) break

    const n = block[0]
    const stack = []
    let max = 0;

    for (let i = 1; i <= n; i++){
        const h = block[i]
        if (!stack.length) {
            stack.push([i, h])
        } else {
            let last = stack.length - 1

            if (stack[last][1] <= h){
                stack.push([i, h])
            } else {
                while (stack.length && stack[last][1] > h){
                    last -= 1
                    const v = stack.pop()
                    let width;

                    if (!stack.length) {
                        width = i - 1
                    } else {
                        width = i - stack[last][0] - 1
                    }

                    max = Math.max(max, v[1] * width)
                }

                stack.push([i, h])
            }
        }
    }


    let last = stack.length - 1
    while (stack.length){
        const v = stack.pop()
        last -= 1

        let width
        if (!stack.length){
            width = n
        } else {
            width = n - stack[last][0]
        }

        max = Math.max(max, width * v[1])
    }

    ans.push(max)
}

console.log(ans.join('\n'))