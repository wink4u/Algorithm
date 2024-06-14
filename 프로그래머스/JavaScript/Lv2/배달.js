class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length;
    }

    swap(idx1, idx2) {
        [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
    }

    add(value) {
        this.heap.push(value);
        this.bubbleUp();
    }

    poll() {
        if (this.heap.length === 1) {
            return this.heap.pop();
        }

        const value = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.bubbleDown();
        return value;
    }

    bubbleUp() {
        let index = this.heap.length - 1;
        let parentIdx = Math.floor((index - 1) / 2);

        while (index > 0 && this.heap[index] < this.heap[parentIdx]) {
            this.swap(index, parentIdx);
            index = parentIdx;
            parentIdx = Math.floor((index - 1) / 2);
        }
    }

    bubbleDown() {
        let index = 0;
        let length = this.heap.length;

        while (true) {
            let leftIdx = 2 * index + 1;
            let rightIdx = 2 * index + 2;
            let smallerIdx = index;

            if (leftIdx < length && this.heap[leftIdx] < this.heap[smallerIdx]) {
                smallerIdx = leftIdx;
            }

            if (rightIdx < length && this.heap[rightIdx] < this.heap[smallerIdx]) {
                smallerIdx = rightIdx;
            }

            if (smallerIdx === index) break;

            this.swap(index, smallerIdx);
            index = smallerIdx;
        }
    }
}


function solution(N, road, K) {
    var answer = 0;
    var node = Array.from(Array(N + 1), () => [])

    road.forEach(([a, b, value]) => {
        node[a].push([b, value])
        node[b].push([a, value])
    })

    const D = new Array(N + 1).fill(1e10)

    const Djkstra = (num) => {
        D[num] = 0
        const heap = new MinHeap();

        heap.add([num, 0])

        while (heap.size() > 0){
            const [now, dist] = heap.poll()

            if (dist > D[now]){
                continue;
            }

            for (let i = 0; i < node[now].length; i++){
                const [next, value] = node[now][i]

                if (dist + value < D[next]) {
                    D[next] = dist + value
                    heap.add([next, dist + value])
                }
            }
        }
    }

    Djkstra(1)

    D.forEach((value) => {
        if (value <= K) answer += 1
    })

    return answer;
}