const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

const [N, M, X] = input[0].split(' ').map(Number)
const arr = input.slice(1).map(v => v.split(' ').map(Number))
const node = Array.from(Array(N + 1), () => [])

for (const [u, v, w] of arr) {
    node[u].push([v, w])
}


class minHeap {
    constructor() {
        this.heap = []
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    size() {
        return this.heap.length
    }

    bubbleUp() {
        let index = this.heap.length - 1
        let parentIdx = Math.floor((index - 1) / 2)

        while (this.heap[parentIdx] && this.heap[parentIdx][1] > this.heap[index][1]) {
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
            (this.heap[leftIdx] && this.heap[leftIdx][1] < this.heap[index][1]) ||
            (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[index][1])
        ) {
            let smallIdx = leftIdx

            if (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[leftIdx][1]){
                smallIdx = rightIdx
            }

            this.swap(index, smallIdx)
            index = smallIdx
            leftIdx = index * 2 + 1
            rightIdx = index * 2 + 2
        }
    }

    add(v) {
        this.heap.push(v)
        this.bubbleUp()
    }

    poll() {
        if (this.size() === 1) {
            return this.heap.pop()
        }

        const v = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()
        return v
    }
}

const result = Array(N + 1).fill(0)

const Djkstra = (x) => {
    const D = Array(N + 1).fill(Infinity)
    D[0] = 0
    D[x] = 0
    const q = new minHeap()
    q.add([x, 0])

    while (q.size()){
        const [now, dist] = q.poll()

        if (D[now] < dist) continue

        for (const [nxt, cost] of node[now]) {
            const total = dist + cost

            if (D[nxt] > total) {
                D[nxt] = total
                q.add([nxt, total])
                
            }
        }
    }

    if (x !== X) result[x] += D[X]
    else {
        for (let i = 1; i <= N; i++){
            result[i] += D[i]
        }
    }

    return D
}

for (let i = 1; i <= N; i++){
    Djkstra(i)
}

console.log(Math.max(...result))