function solution(s) {
    var answer = [];

    const alpha = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine': 9,
    }

    var check = [];

    for (let i = 0; i < s.length; i++){
        if(isNaN(s[i]) === true) {
            check.push(s[i])
        } else {
            answer.push(s[i])
        }


        if (alpha[check.join('')] >= 0) {
            answer.push(alpha[check.join('')])
            check = [];
        }
    }

    const res = parseInt(answer.join(''))

    return res;
}