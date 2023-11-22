import math
# 에라토스테네스 방법
def is_prime_num1(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr

# 소수판별 제곱근을 통해 판별
def is_prime_num2(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def solution(n, k):
    string = ""
    answer = 0
    
    flag = 0
    if k != 10:
        flag = 1
    
    if flag == 1:
        while n > k:
            one = n % k
            n = n // k
            string += str(one)

        string += str(n)

        string = string[::-1]
    else:
        string = str(n)
        
    
    string_split = string.split('0')
    exist_num = []
    string_split.sort()
    
    # 문자열의 길이가 너무 길어서 에라토스테네스는 안됨.
    
    # if string_split[-1].isdigit():
    #     check = is_prime_num(int(string_split[-1]))
    # else:
    #     return 0
    
    for i in string_split:
        if i.isdigit():
            num = int(i)
            if num >= 2 and is_prime_num2(num):
                answer += 1
        
    return answer