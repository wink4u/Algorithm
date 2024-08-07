import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

len_a = len(a)

while True:
    if len(b) == len_a:
        break

    last = b[-1]

    if last == 'B':
        tmp = list(b[:-1])
        tmp.reverse()
        b = ''.join(tmp)
        # b = str(tmp)
    else:
        b = b[:-1]

if a == b:
    print(1)
else:
    print(0)