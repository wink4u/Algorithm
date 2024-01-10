import sys
input = sys.stdin.readline

# N개의 회의실
# 회의실은 9시부터 18시까지만

N, M = map(int, input().split())

room = {}
for i in range(N):
    room[input().strip()] = ['09-10','10-11','11-12','12-13','13-14','14-15','15-16', '16-17', '17-18']


for i in range(M):
    name, start, end = input().split()
    time = int(end) - int(start)
    
    first = int(start)
    for i in range(time):
        if first == 9:
            room[name].remove('0' + str(first) + '-' + str(first + 1))
        else:
            room[name].remove(str(first) + '-' + str(first + 1))
        
        first += 1

sorted_room = sorted(room.items())

for i in range(len(sorted_room)):
    if i != 0:
        print('-----')
    print(f'Room {sorted_room[i][0]}:')
    cnt = 0

    start, end = 0, 0
    exist = []
    for j in range(len(sorted_room[i][1])):
        s, e = sorted_room[i][1][j].split('-')
        if j == 0:
            start, end = int(s), int(e)
        else:
            if int(s) == end:
                end = int(e)
            else:
                if start == 9:
                    exist.append(f'0{start}-{end}')
                else:
                    exist.append(f'{start}-{end}')
                start, end = int(s), int(e)
                cnt += 1
                
    if start == 9:
        exist.append(f'0{start}-{end}')
    else:
        if start != 0:
            exist.append(f'{start}-{end}')
    
    count = len(exist)
    if count:
        print(f'{count} available:')
        for ex in exist:
            print(ex)
    else:
        print('Not available')
                
            