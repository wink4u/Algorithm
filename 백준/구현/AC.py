import sys
from collections import deque
input = sys.stdin.readline

# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수
# 함수 D는 첫 번째 수를 버리는 함수 무조건 배열의 크기가 1이상일때 사용

T = int(input())

for i in range(T):
    command = input()

    list_len = int(input())
    temp = input().strip()

    arr = deque(temp[1:-1].split(","))

    if command.count('D') > list_len:
        print('error')
    else:
        if "R" in command:
            flag = 0
            for t in range(len(command)):
                if command[t] == "R":
                    if flag == 1:
                        flag = 0
                    else:
                        flag = 1

                elif command[t] == "D":
                    if flag == 0:
                        arr.popleft()
                    else:
                        arr.pop()

            if flag == 1:
                arr.reverse()
        else:
            for _ in range(command.count("D")):
                arr.popleft()


        if arr:
            print("[" + ",".join(arr) + "]")
        else:
            print("[]")
