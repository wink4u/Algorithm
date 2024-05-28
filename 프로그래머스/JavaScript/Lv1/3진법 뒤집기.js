function solution(n) {
    var answer = 0;
    const str = n.toString(3).split('').reverse().join('');

    let cnt = 0;

    for (let i = str.length - 1; i >= 0 ; i--){
        if (str[i] === 0) {
            break;
        } else {
            answer += parseInt(str[i]) * (3 ** cnt);
            cnt += 1
        }
    }
    return answer;
}