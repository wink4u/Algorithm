import sys
input = sys.stdin.readline

s = input().strip()

def check(word):
    for i in range(len(word) // 2):
        if word[i] == word[len(word) - 1 -i]:
            pass
        else:
            return False
    return True

def same(word):
    for i in range(1, len(word)):
        if word[0] != word[i]:
            return False
    return True

if check(s):
    if same(s):
        print(-1)
    else:
        print(len(s) - 1)
else:
    print(len(s))