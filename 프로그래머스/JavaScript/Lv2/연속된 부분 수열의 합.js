function solution(sequence, k) {
    var answer = [];
    let [s, e] = [0, 0]

    let value = sequence[s]
    while (s <= e && e < sequence.length) {


        if (value > k) {
            value -= sequence[s]
            s += 1

        } else if (value === k) {
            if (answer.length > 0) {
                if (e - s < answer[1] - answer[0]){
                    answer = [s, e]
                }
            } else {
                answer = [s, e]
            }
            e += 1
            value += sequence[e]

        } else {
            e += 1
            value += sequence[e]
        }

    }
    return answer;
}