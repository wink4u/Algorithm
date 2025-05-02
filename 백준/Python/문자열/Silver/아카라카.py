import sys
input = sys.stdin.readline

ss = input().strip()

def pp(s):
    if len(s) == 1:
        return True

    front = s[:len(s) // 2]
    back = s[len(s) // 2 + 1:] if len(s) % 2 else s[len(s) // 2:]

    if s == s[::-1] and front == front[::-1] and back == back[::-1]:
        return pp(front) and pp(back)
    else:
        return False

if pp(ss):
    print('AKARAKA')
else:
    print('IPSELENTI')