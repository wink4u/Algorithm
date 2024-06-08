import sys

input = sys.stdin.readline

N = int(input())

line = list(map(int, input().split()))


cnt = 0
# for i in range(len(line) - 1, 0, -1):
#     for j in range(i):
#         if (line[j] > line[j + 1]):
#             line[j], line[j + 1] = line[j + 1], line[j]
#             cnt += 1

def merge_sort(arr):

    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        global cnt
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
                cnt += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

print(cnt)