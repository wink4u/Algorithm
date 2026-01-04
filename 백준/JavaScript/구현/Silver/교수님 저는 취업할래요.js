const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.split(' ').map(Number))

let px, py, kx, ky

for (let i = 0; i < N; i++){
    for (let j = 0; j < N; j++){
        if (arr[i][j] === 5) px = i, py = j
        else if (arr[i][j] === 2) kx = i, ky = j
    }
}

const distance = ((px - kx) ** (2) + (py - ky) ** (2)) ** (0.5)
const sx = Math.min(px, kx), sy = Math.min(py, ky)
const ex = Math.max(px, kx), ey = Math.max(py, ky)
let cnt = 0

for (let i = sx; i <= ex; i++){
    for (let j = sy; j <= ey; j++){
        if (arr[i][j] === 1) cnt++
    }
}

if (cnt >= 3 && distance >= 5) console.log(1)
else console.log(0)