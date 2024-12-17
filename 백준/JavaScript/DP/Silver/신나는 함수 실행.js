const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
    input.push(line);
}).on("close", function () {
    const DP = Array.from({ length: 21 }, () => 
    Array.from({ length: 21 }, () => Array.from({ length: 21 }, () => 0)))
    
    const w = (a, b, c) => {
        if (a <= 0 || b <= 0 || c <= 0) {
            return 1
        } 
        if (a > 20 || b > 20 || c > 20) {
            return w(20, 20, 20)
        }
        if (DP[a][b][c]) {
            return DP[a][b][c]
        }
        if (a < b && b < c){
            DP[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return DP[a][b][c]
        }
        DP[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return DP[a][b][c]
    }
    let idx = 0;

    while (true){
        const [a, b, c] = input[idx].split(" ").map(Number)
        if (a === -1 && b === -1 && c === -1) break
        console.log(`w(${a}, ${b}, ${c}) = ${w(a, b, c)}`)
        idx++;
    }
    process.exit();

});
