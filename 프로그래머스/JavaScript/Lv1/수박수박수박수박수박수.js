function solution(n) {
    if (n === 1){
        return '수';
    } else if (n % 2 === 0) {
        return '수박'.repeat(parseInt(n / 2)) ;
    } else {
        return '수박'.repeat(parseInt(n / 2)) + '수';
    }
}