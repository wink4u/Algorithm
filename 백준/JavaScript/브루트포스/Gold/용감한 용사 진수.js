const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, K] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.split(' ').map(Number))

arr.sort((a, b) => {
    if (a[2] !== b[2]) return a[2] - b[2]
})

let ans = Infinity

for (let i = 0; i < N; i++){
    const x = arr[i][0]
    for (let j = 0; j < N; j++){
        const y = arr[j][1]
        let cnt = 0
        let z = 0
        
        for (let k = 0; k < N; k++){
            if (arr[k][0] <= x && arr[k][1] <= y) {
                cnt++
                z = arr[k][2]

                if (cnt === K) break
            }
        }

        if (cnt === K) {
            ans = Math.min(ans, x + y + z)
        }
    }
}

console.log(ans)