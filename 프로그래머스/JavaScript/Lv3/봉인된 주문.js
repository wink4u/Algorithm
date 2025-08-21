function solution(n, bans) {
    var answer = '';
    // hash를 통한 값 체크
    const alp = {}
    for (let i = 97; i < 123; i++){
        alp[String.fromCharCode(i)] = i - 96
    }
    
    // bans 문자열 길이, 문자열 순서 대로 정렬
    const bansSort = [...bans].sort((a, b) =>
               a.length - b.length || a.localeCompare(b))
    
    
    bansSort.forEach((ban) => {
        let v = 0;
        const k = ban.length;
        for (let i = 0; i < k; i++){
            v += 26 ** (k - i - 1) * alp[ban[i]]
        }
        
        if (n >= v) n += 1
        
    })
    
    while (true) {
        const rest = Math.floor(n % 26)
        if (rest === 0) {
            answer += String.fromCharCode(96 + 26)
            n = Math.floor(n / 26) - 1
        } else {
            answer += String.fromCharCode(rest + 96)
            n = Math.floor(n / 26)
        }
        
        if (n === 0) break
        
        if (n < 26) {
            answer += String.fromCharCode(n + 96)
            break
        }
    }
    
    return answer.split('').reverse().join('');
}