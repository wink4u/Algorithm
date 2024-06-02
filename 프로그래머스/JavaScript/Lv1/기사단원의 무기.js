function check(num, limit, pow) {
    let cnt = 0;
    const sqrt = Math.sqrt(num);

    if (num / sqrt === Math.floor(sqrt)) {
        cnt += 1
    }


    for (let i = 1; i < sqrt; i++) {
        if (num % i === 0) {
            cnt += 2
        }

        if (cnt > limit) {
            return pow
        }
    }



    return cnt;
}

function solution(number, limit, power) {
    var answer = 0;

    for (let i = 1; i <= number; i++){
        answer += check(i, limit, power)
    }
    return answer;
}