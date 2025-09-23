const { Console } = require('console');
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = [];

rl.on('line', function(line){
    input.push(line.trim());
}).on('close', function(){
    const [N, M] = input.shift().split(' ').map(Number)
    const exit = input.pop().split(' ').map(Number)

    const parent = Array.from(Array(N + 1), ( _ , i) => i)
    const node = input.map((v) => v.split(' ').map(Number))

    exit.forEach((v, i) => {
        node.push([0, i + 1, v])
    })

    node.sort((a, b) => a[2] - b[2])

    const find = (x) => {
        if (parent[x] === x) return x;
        return parent[x] = find(parent[x])
    }

    const union = (x, y) => {
        x = find(x)
        y = find(y)

        if (x < y) {
            parent[y] = x
        } else {
            parent[x] = y
        }
    }

    let ans = 0;
    for (let i = 0; i < M + N; i++){
        const [u, v, w] = node[i]

        if (find(u) === find(v)) continue;

        union(u, v)
        ans += w;
    }

    console.log(ans)
})