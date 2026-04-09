const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [R, C] = input[0].split(' ').map(Number)
const N = Number(input[1])
const arr = input[2].split(' ').map(Number)

arr.sort((a, b) => a - b)
const visit = Array.from(Array(R), () => Array(C).fill(0))


const check = () => {
    let ans = 0
    let idx = 0

    for (let i = 0; i < R; i++){
        for (let j = 0; j < C; j++){
            while (true) {
                if (idx === N) {
                    return ans
                }

                if (i === 0) {
                    visit[i][j] = arr[idx++]
                    ans++
                    break
                } else {
                    if (visit[i - 1][j] >= arr[idx]) {
                        idx++
                    } else {
                        visit[i][j] = arr[idx++]
                        ans++
                        break
                    }
                }
            }
        }
    }

    return ans
}

console.log(check())

