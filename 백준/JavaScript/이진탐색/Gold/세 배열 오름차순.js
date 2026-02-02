const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, Q] = input[0].split(' ').map(Number)
const arr = []

for (let i = 1; i <= N; i++){
    const parts = input[i].trim().split(/\s+/).map(Number);
    const k = parts[0];
    const tmp = parts.slice(1, 1 + k);
    tmp.sort((a, b) => a - b)
    arr.push(tmp)
}


const ans = []

const check = (array, value) => {
    let left = 0, right = array.length

    while (left < right) {
        const mid = Math.floor((left + right) / 2)

        if (array[mid] <= value) {
            left = mid + 1
        } else {
            right = mid
        }
    }

    return left
}

for (let i = N + 1; i <= N + Q; i++){
    const [a, b, c, j] = input[i].split(' ').map(Number)
    let res = 1
    let left = 1, right = 10 ** 9


    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        const v = check(arr[a - 1], mid) + check(arr[b - 1], mid) + check(arr[c - 1], mid)

        if (v >= j) right = mid;
        else left = mid + 1;

    }

    ans.push(left)
}

console.log(ans.join('\n'))