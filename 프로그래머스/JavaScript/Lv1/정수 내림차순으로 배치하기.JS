function solution(n) {
    const num = n.toString().split('');

    num.sort((a, b) => {
        if (a > b) {
            return b - a;
        }
    })

    const result = parseInt(num.join(''));

    return result;
}