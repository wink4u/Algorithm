function solution(x) {
    var total = 0;
    const arr = x.toString().split('');
    for (let i = 0; i < arr.length; i++) {
        total += parseInt(arr[i])
    }

    if (x % total === 0) {
        return true;
    } else {
        return false;
    }

}