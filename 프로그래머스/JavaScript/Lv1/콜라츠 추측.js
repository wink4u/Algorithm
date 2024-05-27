function solution(num) {
    let cnt = 0;

    while (true) {
        if (cnt === 500){
            return -1
        }

        if (num === 1){
            return cnt
        }


        if (num % 2 === 0) {
            num /= 2
        } else {
            num = num * 3 + 1
        }

        cnt += 1


    }
}