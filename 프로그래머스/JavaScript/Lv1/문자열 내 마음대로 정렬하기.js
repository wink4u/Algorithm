function solution(strings, n) {
    strings.sort((a, b) => {
        const [a_i, b_i] = [a[n], b[n]];
        console.log(a_i, b_i);
        if (a_i < b_i) {
            return -1;
        } else if (a_i > b_i) {
            return 1;
        } else {
            if (a < b) {
                return -1;
            } else if (a > b) {
                return 1;
            } else {
                return 0;
            }
        }
    });

    console.log(strings)
    return strings;
}