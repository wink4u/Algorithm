def gcd(a, b):
    while b:
        r = a % b
        a, b = b, r
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = lcm(answer, i)
    
    return answer