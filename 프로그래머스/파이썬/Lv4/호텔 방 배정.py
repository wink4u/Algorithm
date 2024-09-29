import sys
from collections import defaultdict
sys.setrecursionlimit(10000) # 재귀 허용깊이 임의로 지정

def check_num(num, room):
    if room[num] == 0:
        room[num] = num + 1
        return num
    elif room[num] != 0:
        room[num] = check_num(room[num], room)
        return room[num]

def solution(k, room_number):
    ans = []
    room = defaultdict(lambda : 0)
    for num in room_number:
        ans.append(check_num(num, room))
    return ans