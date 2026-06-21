const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const [N, M] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

const sumA = []
const sumB = []

const mid = Math.floor(N / 2)

const subSet = (idx, end, currentSum, array) => {
    if (idx === end) {
        array.push(currentSum)
        return
    }

    subSet(idx + 1, end, currentSum, array)
    subSet(idx + 1, end, currentSum + arr[idx], array)
}

subSet(0, mid, 0, sumA)
subSet(mid, N, 0, sumB)

sumB.sort((a, b) => a - b)

const binarySearch = (target, flag) => {
    let left = 0
    let right = sumB.length

    // flag가 0이면 lower 1이면 upper
    while (left < right) {
        let mid = Math.floor((left + right) / 2)

        if (flag) {
            if (sumB[mid] > target) {
                right = mid
            } else {
                left = mid + 1
            }
        } else {
            if (sumB[mid] >= target) {
                right = mid
            } else {
                left = mid + 1
            }
        }
    }

    return left
}

let ans = 0

for (let i = 0; i < sumA.length; i++){
    const target = M - sumA[i]
    const cnt = binarySearch(target, 1) - binarySearch(target, 0)
    ans += cnt
}

if (M === 0) ans--

console.log(ans)
