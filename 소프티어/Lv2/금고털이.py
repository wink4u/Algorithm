from collections import defaultdict
import sys
input = sys.stdin.readline

# 배낭무게, 보석 개수
bag, N = map(int, input().split())

# 보석을 담을 list
jew = []


for i in range(N):
    weight, price = map(int, input().split())
    jew.append([price, weight])

# 보석을 가격순으로 정렬
jew.sort(key = lambda x : -x[0])

# 가격을 처리할 변수
price = 0

for i in range(N):
    # 배낭보다 보석 무게가 더 작으면
    if jew[i][1] < bag:
        # 보석무게 전체와 가격값을 처리
        total = jew[i][0] * jew[i][1]
        # 배낭무게에서 보석 무게를 뺌
        bag -= jew[i][1]
        # 가격에 처리된 total값 더함
        price += total
    # 만약 배낭보다 보석이 더 무겁거나 같다면
    else:
        # 남은 배낭의 무게와 보석의 가격값을 처리
        total = bag * jew[i][0]
        # 가격에 처리된 total값 더함
        price += total
        # 배낭에 남은 공간이 없으니 break로 for문을 끝냄
        break

print(price)