const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim().split(/\r?\n/);

const N = Number(input[0]);
const M = Number(input[1]);

const node = Array.from(Array(N + 1), () => Array(N + 1).fill(Infinity));
const parent = Array.from({length : N + 1} , (_, i) => i);

const find = (x) => {
    if (x === parent[x]) return x;
    
    parent[x] = find(parent[x]);

    return parent[x];
}

const union = (a, b) => {
    const pa = find(a);
    const pb = find(b);

    if (pa > pb) {
        parent[pb] = pa
    } else {
        parent[pa] = pb
    }
}

for (let i = 2; i < 2 + M; i++){
    const [a, b] = input[i].split(' ').map(Number);
    node[a][b] = 1;
    node[b][a] = 1;

    union(a, b)
}

const check = Array.from(Array(N + 1), () => []);

for (let k = 1; k <= N; k++){
    const v = find(k);
    check[v].push(k);

    for (let i = 1; i <= N; i++){
        for (let j = 1; j <= N; j++){
            if (node[i][j] > node[i][k] + node[k][j]) {
                node[i][j] = node[i][k] + node[j][j]
            }
        }
    }
}

const answer = []

for (let i = 1; i <= N; i++){
    let person = 0;
    let v = Infinity;

    if (check[i].length) {
        for (const a of check[i]) {
            let tmp = 0
            for (const b of check[i]){
                if (a === b) continue;

                tmp = Math.max(tmp, node[a][b])
            }

            if (v > tmp) {
                person = a
                v = tmp
            }
        }
        answer.push(person)
    }

}

console.log(answer.length)
answer.sort((a, b) => a - b).forEach(v => console.log(v))