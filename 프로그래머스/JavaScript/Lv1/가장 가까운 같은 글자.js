function solution(s) {
    var answer = [];

    var check = {};

    for (let i = 0 ; i < s.length; i++){
        if (check[s[i]] >= 0){
            answer.push(i - check[s[i]])
            check[s[i]] = i
        } else {
            check[s[i]] = i
            answer.push(-1)
        }
    }
    return answer;
}