const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number);
const arr = input.slice(1).map(v => v.split(' ').map(Number))
const set = new Set();

const plusSet = (array) => {
    for (let i = 1; i <= N; i++){
        if (i !== array[0] && i !== array[1]) {
            const v =  [...array, i].sort((a, b) => a - b).join(',')
            set.add(v)
        }
    }
}


for (let i = 0; i < M; i++){
    plusSet(arr[i])
}

const total = (N * (N - 1) * (N - 2)) / 6
console.log(total - set.size)