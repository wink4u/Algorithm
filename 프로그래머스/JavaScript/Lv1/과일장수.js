function solution(k, m, score) {
    var answer = 0;

    score.sort((a, b) => {
        if (a > b) {
            return -1;
        }
    })

    let cnt = 0;
    let value = k;

    for (let i = 0; i < score.length; i++){
        cnt += 1
        value = Math.min(value, score[i])

        if (cnt === m){
            answer += value * cnt;
            cnt = 0;
            value = k;
        }
    }

    return answer;
}