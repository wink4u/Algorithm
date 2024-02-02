import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

best = [0 for _ in range(N)]

for i in range(N):
    people = list(map(int, input().split()))
    
    check_people = defaultdict(int)
    sorted_people = sorted(people, reverse = True)
    
    for j in range(len(people)):
        if not check_people[sorted_people[j]]:
            check_people[sorted_people[j]] = j + 1
        
    for j in range(len(people)):
        best[j] += people[j]
        people[j] = check_people[people[j]]
        

    print(*people)

best_dict = defaultdict(int)
sorted_best = sorted(best, reverse = True)
for i in range(len(best)):
    if not best_dict[sorted_best[i]]:
        best_dict[sorted_best[i]] = i + 1

for i in range(len(best)):
    best[i] = best_dict[best[i]]

print(*best)