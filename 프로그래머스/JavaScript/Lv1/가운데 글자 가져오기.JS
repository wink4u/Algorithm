function solution(s) {
    const len = s.length;
    const middle = parseInt(len / 2);

    if (len % 2 === 0) {
        return s.substring(middle - 1, middle + 1)
    } else {
        return s.substring(middle, middle + 1)
    }

}