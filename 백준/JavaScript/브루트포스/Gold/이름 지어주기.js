const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const N = Number(input.shift())
    const arr = input[0].split(' ').map(Number)
    let [A, B] = input[1].split(' ').map(Number)

    A += A % 2 ? 0 : 1
    B -= B % 2 ? 0 : 1
    arr.sort((a, b) => a - b)

    const check = (num) => {
        if (num < A || num > B) return null // 0 → null로 수정
        if (num % 2) return num

        if (A <= num - 1) return num - 1
        if(num + 1 <= B) return num + 1
        return null // 안전하게 null 반환
    }

    const ans = [];

    for (let i = 0; i < N - 1; i++){
        let tmp = check(Math.floor((arr[i] + arr[i + 1]) / 2))

        if (tmp !== null) {
            // 모든 아들과 비교하도록 수정
            let minDist = Infinity
            for (let j = 0; j < N; j++){
                minDist = Math.min(minDist, Math.abs(tmp - arr[j]))
            }
            ans.push([tmp, minDist])
        }
    }

    let [minA, minB] = [Infinity, Infinity]

    for (let i = 0; i < N; i++){
        minA = Math.min(minA, Math.abs(arr[i] - A))
        minB = Math.min(minB, Math.abs(arr[i] - B))
    }
    
    ans.push([A, minA])
    ans.push([B, minB])

    ans.sort((a, b) => b[1] - a[1])

    console.log(ans[0][0])
    process.exit()
})
