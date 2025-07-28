import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def makeTriangle(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3) / 2

ans = 0
for i in range(1, n - 1):
    ans += makeTriangle(arr[0][0], arr[0][1], arr[i][0], arr[i][1], arr[i + 1][0], arr[i + 1][1])

ans = round(ans, 1)
print(abs(ans))