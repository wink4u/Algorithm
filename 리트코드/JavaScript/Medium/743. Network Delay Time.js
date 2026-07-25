/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
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

        bubbleUp() {
            let index = this.heap.length - 1
            let parentIdx = Math.floor((index - 1) / 2)

            while (this.heap[parentIdx] && this.heap[parentIdx][1] > this.heap[index][1]) {
                this.swap(index, parentIdx)
                index = parentIdx
                parentIdx = Math.floor((index - 1) / 2)
            }
        }

        bubbleDown () {
            let index = 0
            let leftIdx = index * 2 + 1, rightIdx = index * 2 + 2
        
            while (
                (this.heap[leftIdx] && this.heap[leftIdx][1] < this.heap[index][1]) ||
                (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[rightIdx][1])
            ) {
                let smallIdx = leftIdx

                if (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[leftIdx][1]) {
                    smallIdx = rightIdx
                }

                this.swap(index, smallIdx)
                index = smallIdx
                leftIdx = index * 2 + 1, rightIdx = index * 2 + 2
            }
        }

        add(value) {
            this.heap.push(value)
            this.bubbleUp()
        }

        poll() {
            if (this.size() === 1) return this.heap.pop()

            const v = this.heap[0]
            this.heap[0] = this.heap.pop()
            this.bubbleDown()
            return v
        }
    }

    const node = Array.from(Array(n + 1), () => [])
    
    for (const [u, v, w] of times) {
        node[u].push([v, w])
    }

    const q = new minHeap()
    q.add([k, 0])
    const D = new Array(n + 1).fill(Infinity)
    D[0] = 0
    D[k] = 0

    while (q.size()) {
        const [now, dist] = q.poll()

        if (D[now] < dist) continue

        for (const [nxt, cost] of node[now]) {
            const value = dist + cost

            if (D[nxt] > value) {
                D[nxt] = value
                q.add([nxt, value])
            }
        }
    }

    const ans = Math.max(...D)
    return ans === Infinity ? -1 : ans
};