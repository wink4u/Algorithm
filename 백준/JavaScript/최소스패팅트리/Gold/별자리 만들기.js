const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const arr = input.slice(1).map((v) => v.split(' ').map(Number))
const parent = Array.from(Array(N), (v, i) => i)


function find(a) {
    if (a === parent[a]) {
        return a;
    }
    parent[a] = find(parent[a]);
    return parent[a];
}

function union(a, b) {
    const pa = find(a);
    const pb = find(b);

    if (pa < pb) {
        parent[pb] = pa;
    } else {
        parent[pa] = pb;
    }
}

const node = []

for (let i = 0; i < N - 1; i++){
    for (let j = i + 1; j < N; j++){
        const x1 = arr[i][0], y1 = arr[i][1]
        const x2 = arr[j][0], y2 = arr[j][1]

        node.push([Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), i, j])
    }
}


node.sort((a, b) => {
    const a0 = a[0]
    const b0 = b[0]

    if (a0 > b0) return 1
    else return -1
})


const check = () => {
    const ans = [];

    for (let i = 0; i < node.length; i++){
        const [v, s, e] = node[i]

        if (find(s) === find(e)) continue

        ans.push(v)
        union(s, e)

        if(ans.length === N - 1) return ans.reduce((a, b) => a + b, 0).toFixed(2)
    }
}

console.log(check())