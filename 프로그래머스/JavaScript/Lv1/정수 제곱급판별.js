function solution(n) {
    const n_sqrt = Math.sqrt(n);
    if (Number.isInteger(n_sqrt)) {
        return (n_sqrt + 1) ** 2;
    } else {
        return -1
    }
}