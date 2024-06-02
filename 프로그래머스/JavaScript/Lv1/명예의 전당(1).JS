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


function solution(k, score) {
    var answer = [];

    const minheap = new MinHeap();

    for (let i = 0; i < score.length; i++){
        minheap.add(score[i])

        if (minheap.size() > k) {
            minheap.poll();
        }
        answer.push(minheap.heap[0]);
    }

    return answer;
}