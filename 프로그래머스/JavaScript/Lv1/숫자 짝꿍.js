function solution(X, Y) {
    var answer = '';
    X = X.split("")
    Y = Y.split("")

    console.log(X, Y)

    for (let i = 0; i < 10; i++){
        const num_x = X.filter(num => Number(num) === i).length;
        const num_y = Y.filter(num => Number(num) === i).length;
        answer += String(i).repeat(Math.min(num_x, num_y))
    }

    if (answer === '') return "-1"
    if (Number(answer) === 0) return "0"

    return answer.split("").sort((a, b) => Number(b) - Number(a)).join("")

}