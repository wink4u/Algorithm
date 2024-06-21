function solution(lottos, win_nums) {
    var answer = [];

    let [min, zero] = [0, 0];

    for (let i = 0; i < 6; i++){
        const isTrue = lottos[i]

        if (isTrue === 0) zero += 1
        else {
            if (win_nums.includes(isTrue)) min += 1
        }

    }

    console.log(min, zero)

    const c = min > 0 ? 7 - min : 6
    const v = min + zero > 0 ? 7 - (min + zero) : 6
    return [v, c]
}