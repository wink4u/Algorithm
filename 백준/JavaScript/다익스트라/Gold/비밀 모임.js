const fs = require("fs");
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

class minHeap {
    constructor() {
        this.heap = []
    }

    bubbleUp() {
        let index = this.heap.length - 1
        let parentIdx = Math.floor((index - 1) / 2)

        while(this.heap[parentIdx] && this.heap[parentIdx][1] > this.heap[index][1]) {
            this.swap(parentIdx, index)
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

            if (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[smallIdx][1]) {
                smallIdx = rightIdx
            }

            this.swap(smallIdx, index)
            index = smallIdx
            leftIdx = index * 2 + 1
            rightIdx = index * 2 + 2
        }
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    add(value) {
        this.heap.push(value)
        this.bubbleUp()
    }

    poll() {
        if (this.heap.length === 1) {
            return this.heap.pop()
        }

        const v = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()

        return v
    }

    size() {
        return this.heap.length
    }

}


const T = Number(input[0])
let idx = 1

for (let t = 0; t < T; t++){
    const [N, M] = input[idx++].split(' ').map(Number)
    const node = Array.from(Array(N + 1), () => [])
    
    for (let i = 0; i < M; i++){
        const [a, b, c] = input[idx++].split(' ').map(Number)
        node[a].push([b, c])
        node[b].push([a, c])
    }

    const K = Number(input[idx++])
    const friend = input[idx++].split(' ').map(Number)

    const djkstra = (num) => {
        const q = new minHeap()
        const D = Array(N + 1).fill(Infinity)
        D[num] = 0

        q.add([num, 0])

        while(q.size()) {
            const [now, dist] = q.poll()
            if (D[now] < dist) continue

            for (const [nxt, cost] of node[now]) {
                const v = D[now] + cost

                if (v < D[nxt]) {
                    D[nxt] = v
                    q.add([nxt, v])
                }
            }
        }

        return friend.reduce((acc, cur) => acc + D[cur], 0)
    }

    let ans = Infinity
    let room = 0

    for (let i = 1; i <= N; i++){
        const v = djkstra(i)

        if (ans > v) {
            ans = v
            room = i
        }
    }

    console.log(room)
}