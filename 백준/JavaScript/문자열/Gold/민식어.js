const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const N = Number(input[0])
const arr = input.slice(1).map(v => v.trim().replaceAll('ng', 'z').split(''))

const check = {
    'a' : 1, 'b' : 2, 'k': 3, 'd' : 4, 'e' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'l' : 9,
    'm' : 10, 'n' : 11, 'z' : 12, 'o' : 13, 'p' : 14, 'r' : 15, 's' : 16, 't' : 17,
    'u' : 18, 'w' : 19, 'y': 20
}

arr.sort((a, b) => {
    const aLen = a.length
    const bLen = b.length

    const min = Math.min(aLen, bLen) 

    for (let i = 0; i < min; i++){
        const [av, bv] = [check[a[i]], check[b[i]]]

        if (av > bv) {
            return 1
        } else if (av < bv) {
            return -1
        }
    }


    if (aLen < bLen) {
        return -1
    } else {
        return 1
    }
})

console.log(arr.map(v => v.join('').replaceAll('z', 'ng')).join('\n'))