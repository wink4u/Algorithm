function solution(begin, end) {
    var answer = [];

    const check = (value) => {
        let num = 0

        if (value === 1) return 0

        for (let i = 2; i < Math.sqrt(value) + 1; i++){
            if (value % i === 0){
                num = i
                if (value / i <= 1e7){
                    return value / i
                }
            }
        }

        if (num !== 0) return num

        return 1
    }

    for (let i = begin; i <= end; i++){
        answer.push(check(i))
    }
    return answer;
}