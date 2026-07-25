const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split(/\r?\n/);

class minHeap {
    constructor() {
        this.heap = []
    }

    size() {
        return this.heap.length
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]]
    }

    add(v) {
        this.heap.push(v)
        this.bubbleUp()
    }

    poll() {
        if (this.size() === 1) return this.heap.pop()
        
        const v = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()
        return v
    }

    bubbleUp() {
        let idx = this.heap.length - 1
        let parentIdx = Math.floor((idx - 1) / 2)

        while (this.heap[parentIdx] && this.heap[parentIdx][0] > this.heap[idx][0]) {
            this.swap(idx, parentIdx)
            idx = parentIdx
            parentIdx = Math.floor((idx - 1) / 2)
        }
    }

    bubbleDown() {
        let idx = 0
        let leftIdx = idx * 2 + 1, rightIdx = idx * 2 + 2

        while (
            (this.heap[leftIdx] && this.heap[leftIdx][0] < this.heap[idx][0]) ||
            (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[idx][0])
        ) {
            let smallIdx = leftIdx

            if (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[leftIdx][0]) {
                smallIdx = rightIdx
            }

            this.swap(idx, smallIdx)
            idx = smallIdx
            leftIdx = idx * 2 + 1
            rightIdx= idx * 2 + 2
        }
    }
}


const [N, M] = input[0].split(' ').map(Number)
const node = input.slice(1).map(v => v.split(' ').map(Number))
const path = Array(N).fill(-1)

const djkstra = () => {
    const q = new minHeap()
    q.add([0, 0])
    
    const D = Array(N).fill(Infinity)
    D[0] = 0


    while (q.size()) {
        const [dist, now] = q.poll()

        if (D[now] < dist) continue

        for (let nxt = 0; nxt < N; nxt++){
            const cost = node[now][nxt]

            if (D[nxt] > dist + cost) {
                D[nxt] = dist + cost
                q.add([dist + cost, nxt])
                path[nxt] = now
            }
        }
    }

    return D[M - 1]
}


console.log(djkstra())

let now = M - 1
const ans = [M]

while (now !== 0){
    const nxt = path[now]
    ans.push(nxt + 1)
    now = nxt 
}

console.log(ans.reverse().join(' '))