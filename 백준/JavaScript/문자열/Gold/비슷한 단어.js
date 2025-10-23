const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const n = Number(input[0])
const arr = input.slice(1).map((v, i) => [v.trim(), i])
                        .sort((a, b) => {
                            if (a[0] > b[0]) return 1
                            if (a[0] < b[0]) return -1
                            return 0
                        })

let ans = []
let tmp = ['', '']
let length = 0;
let first = Infinity;
let second = Infinity

const compare = (a, b) => {
    const min = Math.min(a[0].length, b[0].length)
    let cnt = 0;
    for (let i = 0; i < min; i++){
        if (a[0][i] !== b[0][i]) break
        cnt++
    }

    if (cnt > length) {
        length = cnt
        first = a[1]
        second = b[1]
        ans = [a[0], b[0]]
    } else if (cnt === length){
        if (first > a[1]) {
            first = a[1]
            second = b[1]
            ans = [a[0], b[0]]
        } else if (first === a[1] && second > b[1]) {
            first = a[1]
            second = b[1]
            ans = [a[0], b[0]]
        }
    }

}

for (let i = 0; i < n - 1; i++){
    const a = arr[i]
    
    if (i === 0){
        tmp[a[1]] = a[0]
    }

    for (let j = i + 1; j < n; j++){
        const b = arr[j]

        if (a[0][0] !== b[0][0]) break

        if (a[1] < b[1]){
            compare(a, b)
        } else {
            compare(b, a)
        }

        if (b[1] === 0 || b[1] === 1){
            tmp[b[1]] = b[0]
        }
    }


}

if (ans.length){
    console.log(ans[0])
    console.log(ans[1])
} else {
    console.log(tmp[0])
    console.log(tmp[1])
}