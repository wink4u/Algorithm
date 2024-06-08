import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

time = 0
bridge = [0] * w

while bridge:
    time += 1
    bridge.pop(0)

    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)

print(time)