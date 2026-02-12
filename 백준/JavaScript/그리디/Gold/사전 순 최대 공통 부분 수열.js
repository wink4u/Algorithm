const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const A = Number(input[0])
const arr1 = input[1].split(' ').map(Number)
const B = Number(input[2])
const arr2 = input[3].split(' ').map(Number)

let idx1 = 0
let idx2 = 0

const test = []
while (idx1 !== A) {
    let max = 0
    let i1 = 0, j1 = 0

    for (let i = idx1; i < A; i++){
        for (let j = idx2; j < B; j++){
            if (arr1[i] === arr2[j]) {
                if (max < arr1[i]) {
                    max = arr1[i]
                    i1 = i + 1
                    j1 = j + 1
                    break
                }
            }
        }
    }


    if (!max) break

    test.push(max)
    idx1 = i1
    idx2 = j1
}

if (test.length) {
    console.log(test.length)
    console.log(test.join(' '))
} else {
    console.log(0)
}