/**
 * @param {number[][]} edges
 * @param {boolean[]} online
 * @param {number} k
 * @return {number}
 */
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

    poll() {
        if (this.heap.length === 1) return this.heap.pop()

        const v = this.heap[0]
        this.heap[0] = this.heap.pop()
        this.bubbleDown()

        return v
    }

    add(v) {
        this.heap.push(v)
        this.bubbleUp()
    }

    bubbleUp() {
        let index = this.heap.length - 1
        let parentIdx = Math.floor((index - 1) / 2)


        while (this.heap[parentIdx] &&
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

var findMaxPathScore = function(edges, online, k) {
    let ans = -1

    const n = online.length
    const node = Array.from(Array(n), () => [])
    const weights = new Set()

    for (const [u, v, w] of edges) {
        if (online[u]) node[u].push([v, w])
        weights.add(w)
    }

    const sortedWeight = Array.from(weights).sort((a, b) => a - b)

    console.log(node)

    const djkstra = (target) => {
        const d = Array(n).fill(Infinity)
        const heap = new minHeap();

        d[0] = 0
        heap.add([0, 0])

        while (heap.size() > 0) {
            const [dist, now] = heap.poll()

            if (dist > d[now]) continue
            if (now === n - 1) return dist <= k;

            for (const [nxt, w] of node[now]) {
                if (w < target) continue

                const cost = dist + w

                if (cost < d[nxt]) {
                    d[nxt] = cost
                    heap.add([cost, nxt])
                }
            }
        }

        return d[n - 1] <= k
    }

    let left = 0, right = sortedWeight.length - 1

    while (left <= right) {
        const mid = (left + right) >> 1;

        if (djkstra(sortedWeight[mid])) {
            ans = sortedWeight[mid]
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return ans
};  