const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [N, M] = input[0].split(' ').map(Number)
const king = input[1].trim()

const node = {}
const visit = {}
const indegree = {}

function init(name) {
    if (!(name in node)) node[name] = [];
    if (!(name in indegree)) indegree[name] = 0;
    if (!(name in visit)) visit[name] = 0;
}

for (let i = 2; i < 2 + N; i++) {
    const [child, mother, father] = input[i].trim().split(" ");

    init(child);
    init(mother);
    init(father);

    node[mother].push(child);
    node[father].push(child);
    indegree[child] += 2;
}

visit[king] = 1;
const q = [];

for (const name in indegree) {
    if (indegree[name] === 0) q.push(name);
}

let idx = 0;

while (idx < q.length) {
    const now = q[idx++];

    for (const nxt of node[now]) {
        visit[nxt] += visit[now] / 2;
        indegree[nxt]--;

        if (indegree[nxt] === 0) {
            q.push(nxt);
        }
    }
}

let max = -1;
let ans;

for (let i = 2 + N; i < 2 + M + N; i++){
    const v = input[i].trim()

    init(v);

    if (visit[v] > max) {
        max = visit[v];
        ans = v;
    }
}

console.log(ans)