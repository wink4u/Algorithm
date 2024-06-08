import sys
input = sys.stdin.readline

sentence = input().split('-')

numbers = []

for i in sentence:
    temp = 0

    each = i.split('+')
    for j in each:
        temp += int(j)

    numbers.append(temp)

result = numbers[0]

for i in range(1, len(numbers)):
    result -= numbers[i]

print(result)

