function solution(w, h) {
    var answer = w * h;

    if (w === h) {
        return w * h - (Math.min(w, h))
    }

    const gcd = (a, b) => {
        while(b !== 0){
            const temp = b;
            b = a % b;
            a = temp;
        }

        const x = Math.floor(w / a)
        const y = Math.floor(h / a)

        return a * (x + y - 1);
    }

    const value = gcd(w, h)

    return answer - (value);
}
