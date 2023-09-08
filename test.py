from itertools import permutations

max_v = 0
def check(a, b, cals):
    if cals == '+':
        return str(int(a) + int(b))
    elif cals == '-':
        return str(int(a) - int(b))
    elif cals == '*':
        return str(int(a) * int(b))

def calu(expression, calcul):
    global max_v
    arr = []
    number = ''

    for i in expression:
        if i.isdigit():
            number += i
        else:
            arr.append(number)
            arr.append(i)
            number = ''

    arr.append(number)

    for o in calcul:
        stack = []
        while len(arr) != 0:
            tmp = arr.pop(0)
            if tmp == o:
                stack.append(check(stack.pop(), arr.pop(0), o))
            else:
                stack.append(tmp)

            print(stack)
        arr = stack

    max_v = max(max_v, abs(int(arr[0])))

def solution(expression):
    cal = ['-', '+', '*']
    cal = list(permutations(cal, 3))

    for i in cal:
        calu(expression, i)
    print(max_v)

