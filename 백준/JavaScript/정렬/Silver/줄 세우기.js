const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.trim())

const isRight = (a, b) => {
    for (let i = 0; i < N; i++){
        if (a[i] !== b[i]) return false
    }

    return true
}

const checkSort = (v) => {
    const one = [...v].sort((a, b) => a.localeCompare(b))
    if (isRight(v, one)) return 'INCREASING'
    
    const two = [...v].sort((a, b) => b.localeCompare(a))
    if (isRight(v, two)) return 'DECREASING'

    return 'NEITHER'
}

console.log(checkSort(arr))