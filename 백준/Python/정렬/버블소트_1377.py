import sys
input = sys.stdin.readline

# arr의 길이
N = int(input())
arr = []
# arr에 길이와 index를 넣어준다
for i in range(N):
    arr.append((int(input()), i))

re_arr = sorted(arr)

max_v = 0
# 버블 소트를 하면 시간복잡도가 N^2이 되므로 당연히 시간초과가 남
# 정렬의 결과를 인덱스의 차이를 통해 얼마나 전환되는건지 파악하면 됨
# 이 개념을 알기 위해선 직접 해봐야 암.. 블로그를 참조해서 개념을 배움!
for i in range(N):
    max_v = max(re_arr[i][1] - arr[i][1], max_v)

print(max_v + 1)