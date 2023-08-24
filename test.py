import sys
input = sys.stdin.readline

G = int(input())

P = int(input())

gate = [i for i in range(G + 1)]
ans = 0
for _ in range(P):
    air = int(input())

    if not gate[air]:
        gate[air] -= 1
    else:
        for i in range(air - 1, 0, -1):
            if not gate[i]:
                gate[i] += 1
                break

        else:
            break

print(sum(gate))
# print(gate)


# plane = []
# prev = int(input())
# count = 1
# new_p = [prev, count]
# for i in range(P - 1):
#     air = int(input())
#
#     if prev != air:
#         prev = air
#         plane.append(new_p)
#         count = 1
#         new_p = [air, count]
#     else:
#         new_p[1] += 1
#
#     if i == P - 2:
#         plane.append(new_p)
#
# print(plane)
# ans = 0
# for i in range(len(plane)):



