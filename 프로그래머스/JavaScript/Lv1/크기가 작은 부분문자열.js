function solution(t, p) {
    var answer = 0;

    for (let i = 0; i < t.length - p.length + 1; i++){
        const test = t.slice(i, i + p.length);

        if (parseInt(test) <= parseInt(p)) {
            answer++;
        }
    }
    return answer;
}