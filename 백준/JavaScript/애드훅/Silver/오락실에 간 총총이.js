const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map((v) => v.trim().split(''))

let totalCnt = 0
let rowCnt = 0, colCnt = 0

for (let i = 0; i < N; i++){
    const cnt = arr[i].filter((v) => v === 'G').length

    if (cnt > 0) rowCnt++

    totalCnt += cnt
}

if (totalCnt === 1) {
    console.log(0)
    process.exit()
}


const newArr = arr.map((_, col) => arr.map(row => row[col]))

for (let i = 0; i < N; i++){
    const cnt = newArr[i].filter((v) => v === 'G').length

    if (cnt > 0) {
        colCnt++

        if (colCnt > 1) break
    }
}



const check = (array) => {
    let cnt1 = 0, cnt2 = 0;
    
    for (let i = 0; i < N; i++){
        const v = array[i].filter(value => value === '.').length;
    
        if (v === N) cnt1++
        else break
    }

    for (let i = N - 1; i >= 0; i--) {
        const v = array[i].filter(value => value === '.').length;
    
        if (v === N) cnt2++
        else break
    }

    return Math.max(cnt1, cnt2)
}

if (rowCnt === 1) {
    console.log(N - 1 - check(newArr))
} else if (colCnt === 1) {
    console.log(N - 1 - check(arr))
} else {
    console.log((N - 1 - check(arr)) + (N - 1 - check(newArr)))
}
