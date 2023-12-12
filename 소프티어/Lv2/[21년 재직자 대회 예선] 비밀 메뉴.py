import sys
input = sys.stdin.readline

# 자판기에는 총 K개의 버튼
# 각 버튼마다 1부터 K까지의 번호가 붙어있음

# 비밀메뉴 조작법은 M개의 버튼 조작

# 사용자가 누른 N개의 버튼 조작

M, N, K = map(int, input().split())

secret = input().strip()

s_len = len(secret)

numbers = input()
flag = 0

if s_len <= len(numbers):
  if secret in numbers:
    flag = 1

if flag == 0:
  print('normal')
else:
  print('secret')