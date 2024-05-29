function solution(s, n) {
    var answer = [];

    for (let i = 0; i < s.length; i++) {
        if(s[i] === ' '){
            answer.push(s[i])
            continue
        }

        const ASCII = s[i].charCodeAt();
        let res = ASCII + n;
        if (ASCII >= 97){
            if (res > 122){
                res -= 26
            }

        } else {
            if (res > 90) {
                res -= 26
            }
        }

        answer.push(String.fromCharCode(res));
    }

    return answer.join('');
}