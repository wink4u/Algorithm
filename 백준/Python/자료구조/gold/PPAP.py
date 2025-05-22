import sys
input = sys.stdin.readline

s = input().strip()
before = []

if len(s) < 4:
    if s == 'P':
        print('PPAP')
    else:
        print('NP')
else:
    for i in range(len(s)):
        if s[i] == 'P':
            before.append('P')
        else:
            if 2 <= i <= len(s) - 2:
                if len(before) < 2:
                    print('NP')
                    exit()
                else:
                    if s[i + 1] != 'P':
                        print('NP')
                        exit()
                    else:
                        for _ in range(2):
                            before.pop()
            else:
                print('NP')
                exit()

    if before:
        if len(before) == 1:
            print('PPAP')
        else:
            print('NP')
    else:
        print('PPAP')