function solution(a, b) {
    var answer = 0;

    const [s, e] = [Math.min(a, b), Math.max(a,b)];

    for (let i = s; i <= e; i++){
        answer += i
    }
    return answer;
}