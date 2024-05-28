function solution(s) {
    var answer = '';

    const list = s.split('');

    list.sort((a , b) => b.charCodeAt(0) - a.charCodeAt(0))

    return list.join('');
}