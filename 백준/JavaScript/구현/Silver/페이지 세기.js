const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

let idx = 0

while (true) {
    const num = Number(input[idx++])

    if (!num) break

    const v = Array(num + 1).fill(0)
    const arr = input[idx++].split(',')

    for (let i = 0; i < arr.length; i++){
        if (!arr[i].includes('-')) {
            const x = Number(arr[i])
            if (x <= num) v[x] = 1
            continue
        }
        
        const [l, r] = arr[i].split('-').map(Number)

        if (l <= r && l <= num) {
            for (let j = l; j <= Math.min(r, num); j++){
                v[j] = 1
            }
        }
    }

    console.log(v.reduce((a, b) => a + b, 0))
}