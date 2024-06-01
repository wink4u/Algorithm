function solution(food) {
    var answer = [];

    for (let i = 1; i < food.length; i++){
        const res = parseInt(food[i] / 2)
        if (res > 0) {
            const test = i.toString().repeat(res)
            answer.push(test);
        }
    }

    var reverse = answer.slice().reverse();

    return answer.join('') + '0' + reverse.join('');
}