function solution(s) {

    var arr = [];
    let start = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' '){
            arr.push(s[i])
            start = 0
            continue
        }

        if (start % 2 === 0){
            arr.push(s[i].toUpperCase())
        } else {
            arr.push(s[i].toLowerCase())
        }
        start += 1
    }

    return arr.join('');
}