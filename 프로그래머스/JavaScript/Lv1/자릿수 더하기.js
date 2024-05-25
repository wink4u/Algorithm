function solution(n)
{
    var answer = 0;
    var test =  n.toString().split('')

    for (let i = 0; i < test.length; i++){
        answer += parseInt(test[i])
    }
    return answer;
}