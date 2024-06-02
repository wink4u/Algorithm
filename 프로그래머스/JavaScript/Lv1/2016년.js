function solution(a, b) {
    var date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    var cnt = b - 1;

    for (let i = 1; i < a; i++) {
        cnt += date[i]
    }

    console.log(cnt);
    console.log(cnt % 7);
    const answer = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return answer[cnt % 7];
}