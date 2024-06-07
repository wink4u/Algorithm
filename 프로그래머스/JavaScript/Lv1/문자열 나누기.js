function solution(s) {
    var answer = 0;
    let flag = 0;

    let alpha = ''
    let [total, cnt] = [0, 0];
    for (let i = 0; i < s.length; i++){
        if (flag === 0) {
            alpha = s[i];
            total += 1
            flag = 1;
        } else {
            if (alpha === s[i]) {
                total += 1
            } else {
                cnt += 1
            }

            if (total === cnt) {
                flag = 0
                answer += 1
            }
        }

    }

    return flag === 1 ? answer + 1 : answer;
}