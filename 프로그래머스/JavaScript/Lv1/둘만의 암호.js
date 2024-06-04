function solution(s, skip, index) {
    var answer = [];

    const string = s.split('')
    const test = skip.split('')

    for (let i = 0; i < string.length; i++) {
        let tmp = string[i].charCodeAt();
        let cnt = 0;
        while (true) {
            tmp += 1

            if (tmp > 122) {
                tmp = 97
            }

            if (test.includes(String.fromCharCode(tmp)) === false) {
                cnt += 1
                if (cnt === index) {
                    answer.push(String.fromCharCode(tmp))
                    break;
                }
            }
        }
    }

    return answer.join('');
}