from itertools import permutations
cal = ['-', '+', '*']
op = list(permutations(cal, 3))

def first(temp):
    if len(temp) == 3:
        print(temp)
        return

    for i in range(len(cal)):
        if cal[i] not in temp:
            temp.append(cal[i])
            first(temp)
            temp.pop()

first([])