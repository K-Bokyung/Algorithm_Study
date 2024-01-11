# https://www.acmicpc.net/problem/10799

import sys

pipe = sys.stdin.readline().rstrip()
stack = []
result = 0

for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if pipe[i-1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)
