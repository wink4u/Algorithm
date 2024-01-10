import sys

input = sys.stdin.readline
# 테스트케이스 숫자
T = int(input())

numbers = {'0':[0,1,2,3,4,5], '1':[4,5], '2':[0,2,3,5,6], '3':[0,3,4,5,6], '4':[1,4,5,6], '5':[0,1,3,4,6], '6':[0,1,2,3,4,6]
           ,'7':[0,1,4,5], '8':[0,1,2,3,4,5,6], '9':[0,1,3,4,5,6], 'X':[]}

for i in range(T):
    A, B = map(int, input().split())
    A_list, B_list = [], []    
    minus = len(str(A)) - len(str(B))
    if minus > 0:
        for i in range(minus):
            B_list.append('X')
    elif minus < 0:
        for i in range(-minus):
            A_list.append('X')
        
    A_list = A_list + list(str(A))
    B_list = B_list + list(str(B))

    result = 0
    for i in range(len(A_list)):
        if A_list[i] == B_list[i]:
            continue

        a_num = numbers.get(A_list[i])
        b_num = numbers.get(B_list[i])

        if len(a_num) == 0 or len(b_num) == 0:
            result += abs(len(a_num) - len(b_num))
            continue

        cnt = 0
        for j in range(len(b_num)):
            if b_num[j] in a_num:
                cnt += 2

        result += abs(len(a_num) + len(b_num) - cnt)

    print(result)

    