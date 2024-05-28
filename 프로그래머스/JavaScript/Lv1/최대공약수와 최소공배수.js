function solution(n, m) {
    let LCM = (num1, num2) => {
        let check = 1;

        while(true) {
            if((check % num1 === 0) && (check % num2 === 0)) {
                break;
            }
            check++;
        }
        return check;
    }

    let GCD = (num1, num2) => {
        while(num2 > 0) {
            let r = num1 % num2;
            num1 = num2;
            num2 =r;
        }
        return num1;
    }

    return [GCD(n,m),LCM(n,m)];
}