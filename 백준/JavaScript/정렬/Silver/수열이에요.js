const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, L, R] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

if (N === 1) {
    console.log(1)
    process.exit()
}

let flag = 1

const check = (num) => {
    return num >= L - 1 && num <= R - 1
}
for (let i = 0; i < N - 1; i++){
    if (arr[i] > arr[i + 1]) {
        if (!check(i) || !check(i + 1)) {
            flag = 0
            break
        }
    }
}


console.log(flag)