import sys
from collections import defaultdict
input = sys.stdin.readline

message = input().strip()
key = input().strip()
alpha = defaultdict(list)

board = [[] for _ in range(5)]

line = 0
for i in range(len(key)):
    if not alpha[key[i]]:
        board[line].append(key[i])
        alpha[key[i]] = (line, len(board[line]) - 1)
        if len(board[line]) == 5:
            line += 1

for i in range(65, 91):
    value = chr(i)
    if value != 'J':
        if not alpha[value]:
            board[line].append(value)
            alpha[value] = (line, len(board[line]) - 1)
            if len(board[line]) == 5:
                line += 1

i = 0
while i < len(message)-1:
    if message[i] == message[i+1]:
        if message[i] != 'X':
            message = message[:i+1] + 'X' + message[i+1:]
        else:
            message = message[:i+1] + 'Q' + message[i+1:]
    else:
        i += 2

if len(message) % 2:
    message = message + 'X' 

# message = ''
# flag = 0
# for i in range(len(msg) - 1):
#     if flag:
#         if i == len(msg) - 2:
#             message += msg[i + 1]
#         flag = 0
#     else:
#         if msg[i] == msg[i + 1]:
#             message += msg[i]
#             if msg[i] == 'X':
#                 message += 'Q'
#             else:
#                 message += 'X'
#         else:
#             message += msg[i]
#             message += msg[i + 1]
#             flag = 1

# if len(message) % 2:
#     message += 'X'

answer = ''

for i in range(0, len(message), 2):
    x1, y1 = alpha[message[i]]
    x2, y2 = alpha[message[i + 1]]

    if x1 == x2:
        answer += board[x1][(y1+1)%5]
        answer += board[x2][(y2+1)%5]
    elif y1 == y2:
        answer += board[(x1+1)%5][y1]
        answer += board[(x2+1)%5][y2]
    else:
        answer += board[x1][y2]
        answer += board[x2][y1]

print(answer)