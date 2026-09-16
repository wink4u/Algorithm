const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

let idx = 0
for (let i = 0; i < 4; i++){
    const aNum = Number(input[idx])
    const aArr = input.slice(idx + 1, idx + 1 + aNum).map(Number)
    idx += 1 + aNum
    const bNum = Number(input[idx])
    const bArr = input.slice(idx + 1, idx + 1 + bNum).map(Number)
    idx += 1 + bNum

    aArr.sort((a, b) => a - b)
    bArr.sort((a, b) => a - b)
    
    const check = () => {
        let aIdx = 0
        let bIdx = bNum - 1
        
        while (aIdx < aNum && bIdx >= 0) {
            const v = aArr[aIdx] + bArr[bIdx]

            if (v == 10000) {
                return 'YES'
            }

            if (v < 10000) {
                aIdx++
            } else {
                bIdx--
            }
        }

        return 'NO'
    }

    console.log(check())

}