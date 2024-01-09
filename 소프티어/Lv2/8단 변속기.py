import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
num = numbers[0]
state = 'ascending'

if num == 8:
    state = 'descending'

for i in range(1, len(numbers)):
    if state == 'ascending':
        if num > numbers[i]:
            state = 'mixed'
            break
        else:
            num = numbers[i]
    elif state == 'descending':
        if num < numbers[i]:
            state = 'mixed'
            break
        else:
            num = numbers[i]

print(state)