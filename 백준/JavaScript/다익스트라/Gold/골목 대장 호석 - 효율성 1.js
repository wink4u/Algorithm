const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

class MinHeap {
    constructor() {
        this.heap = []
    }

    size() {
        return this.heap.length
    }

    add(value) {
        this.heap.push(value)
        this.bubbleUp()
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
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

    bubbleUp() {
        let index = this.size() - 1
        let parentIdx = Math.floor((index - 1) / 2)

        while (
            this.heap[parentIdx] &&
            this.heap[parentIdx][0] > this.heap[index][0]
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

            if (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[smallIdx][0]) {
                smallIdx = rightIdx
            }

            this.swap(index, smallIdx)
            index = smallIdx
            leftIdx = index * 2 + 1
            rightIdx = index * 2 + 2

        }
    }
}


const [N, M, A, B, C] = input[0].split(' ').map(Number)
const node = Array.from(Array(N + 1), () => [])
for (let i = 1; i <= M; i++){
    const [a, b, v] = input[i].split(' ').map(Number)
    node[a].push([b, v])
    node[b].push([a, v])
}

const djkstra = (limit) => {
    const D = Array(N + 1).fill(Infinity)
    const visit = Array(N + 1).fill(0)

    visit[A] = 1
    D[A] = 0

    const q = new MinHeap()
    q.add([0, A])

    while (q.size()) {
        const [dist, now] = q.poll()

        visit[now] = 1

        if (now === B && D[now] <= C) return true

        if (D[now] < dist) {
            continue
        }

        for (const [nxt, v] of node[now]) {
            if (visit[nxt] || v > limit) continue

            const cost = dist + v

            if (D[nxt] > cost) {
                D[nxt] = cost
                q.add([cost, nxt])
            }
        }
    }

    return false
}

let left = 1, right = 21

while (left < right) {
    const mid = Math.floor((left + right) / 2)

    if (djkstra(mid)) {
        right = mid
    } else {
        left = mid + 1
    }
}

console.log(right === 21 ? -1 : right)