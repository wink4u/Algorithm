const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const s = input[1].trim()

const check = Array(26).fill(0)

let left = 0, right = 0
const set = new Set()

let ans = 0

while (left <= right && right < s.length) {
    const now = s[right]
    set.add(now)
    const num = now.charCodeAt()
    check[num - 97] += 1

    while (set.size > N) {
        const leftNum = s[left].charCodeAt() - 97
        check[leftNum] -= 1
        if (check[leftNum] === 0) {
            set.delete(s[left])
        }
        left += 1
    }
    

    ans = Math.max(ans, right - left + 1)
    right += 1
}

console.log(ans)