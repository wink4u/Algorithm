import sys
input = sys.stdin.readline

n = int(input())
node = {}

for _ in range(n):
    a, b, c = input().strip().split()
    node[a] = [b, c]

def preorder(root):
    if root != '.':
        print(root, end = '')
        preorder(node[root][0])
        preorder(node[root][1])

def inorder(root):
    if root != '.':
        inorder(node[root][0])
        print(root, end = '')
        inorder(node[root][1])

def postorder(root):
    if root != '.':
        postorder(node[root][0])
        postorder(node[root][1])
        print(root, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')