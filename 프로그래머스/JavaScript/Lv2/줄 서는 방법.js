function solution(n, k) {
    var answer = [];
    const fact = [1];
    
    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i;
    }    
    
    const nums = Array.from({ length: n }, (_, i) => i + 1);
    const ans = [];
    let kk = k - 1;
    
    for (let m = n; m >= 1; m--) {
        const t = fact[m - 1];               
        const idx = Math.floor(kk / t);      
        answer.push(nums.splice(idx, 1)[0]);     
        kk %= t;                                
    }
    
    return answer;
}

