function solution(n, left, right) {
    var answer = [];

    for (let i = left; i <= right; i++){
        const [value, rest] = [Math.floor(i / n), i % n]

        let check = value - rest < 0 ? 0 : value - rest
        answer.push(check + rest + 1)

    }


    return answer;
}