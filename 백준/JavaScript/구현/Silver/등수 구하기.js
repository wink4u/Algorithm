const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, score, P] = input[0].split(' ').map(Number)
if (N === 0) {
    console.log(1)
    process.exit()
}

const list = input[1].split(' ').map(Number).reverse()

const check = (arr) => {
    let cnt = 0;
    let place = 1;
    let flag = 0;

    while (cnt !== P && arr.length){
        const v = arr.pop()
    
        if (v > score){
            place++
        } else if(v < score){
            return place
        } 
        cnt++
    }

    return cnt < P ? place : -1
}

console.log(check(list))