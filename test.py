
# gcb 유클리드

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
print(gcd(22, 8))