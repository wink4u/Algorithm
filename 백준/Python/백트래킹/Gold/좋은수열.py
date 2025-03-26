import sys
input = sys.stdin.readline

n = int(input())
res = float('inf')

def check(br):
    br = ''.join(map(str, br))
    bl = len(br)
    m = bl // 2
    for i in range(1, m + 1):
        if br[bl - i * 2: bl - i] == br[bl - i:]:
            return False
    return True

def back(num):
    global res

    if len(num) == n:
        print(num)
        exit()

    for i in (1, 2, 3):
        if check(num + str(i)):
            back(num + str(i))

back('1')

