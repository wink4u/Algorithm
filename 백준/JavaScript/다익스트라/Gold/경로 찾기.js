const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const [N, K] = input[0].split(' ').map(Number)
const node = Array.from(Array(N), () => [])
const code = input.slice(1, N + 1).map((v) => v.trim())
const [s, e] = input[N + 1].split(' ').map(Number)

class MinHeap {
    constructor() {
        this.heap = [];
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    size() {
        return this.heap.length;
    }

    add(value) {
        this.heap.push(value)
        this.bubbleUp()
    }

    poll() {
        if (this.heap.length === 1) {
            return this.heap.pop()
        }

        const value = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()
        return value
    }

    bubbleUp() {
        let index = this.heap.length - 1
        let parentIdx = Math.floor((index - 1) / 2)

        while (
            this.heap[parentIdx] &&
            this.heap[parentIdx][0] < this.heap[index][0]
        ) {
            this.swap(index, parentIdx)
            index = parentIdx
            parentIdx = Math.floor((index - 1) / 2)
        }
    }

    bubbleDown() {
        let index = 0
        let leftIdx = index * 2 + 1
        let rightIdx = index * 2 + 2

        while (
            (this.heap[leftIdx] && this.heap[leftIdx][0] < this.heap[index][0]) ||
            (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[index][0])
        ) {
            let smallIdx = leftIdx

            if (
                this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[leftIdx][0]
            ) {
                smallIdx = rightIdx
            }

            this.swap(smallIdx, index)
            index = smallIdx
            leftIdx = index * 2 + 1
            rightIdx = index * 2 + 2
        }
    }

}


for (let i = 0; i < N - 1; i++){
    for (let j = i + 1; j < N; j++){
        let cnt = 0
        for (let k = 0; k < K; k++){
            if (code[i][k] !== code[j][k]) cnt++

            if (cnt > 1) break
        }

        if (cnt === 1) {
            node[i].push(j)
            node[j].push(i)
        }
    }
}

const djkstra = () => {
    const D = Array(N).fill(Infinity)
    D[s - 1] = 0
    const q = new MinHeap()
    q.add([0, s - 1])
    const path = Array(N).fill(-1)

    while (q.size()) {
        const [dist, now] = q.poll()

        if (D[now] < dist) {
            continue
        }

        for (const nxt of node[now]) {
            const cost = dist + 1

            if (D[nxt] > cost) {
                D[nxt] = cost
                path[nxt] = now
                q.add([cost, nxt])
            }
        }
    }

    return path
}


const ans = [e]
const check = djkstra()
let now = e - 1
while (true) {
    const nxt = check[now]
    if (nxt === -1) break

    ans.push(nxt + 1)
    now = nxt
}

if (ans.length === 1) {
    console.log(-1)
} else {
    console.log(ans.reverse().join(' '))
}