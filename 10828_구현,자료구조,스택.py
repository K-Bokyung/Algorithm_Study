# https://www.acmicpc.net/problem/10828

# 1
import sys

n = int(input())
s = []

for _ in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        s.append(order[1])
        
    elif order[0] == 'pop':
        if len(s) > 0:
            print(s.pop())
        else:
            print(-1)
            
    elif order[0] == 'size':
        print(len(s))
        
    elif order[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
            
    elif order[0] == 'top':
        if len(s) > 0:
            print(s[-1])
        else:
            print(-1)

# 2
import sys

N = int(sys.stdin.readline())
result = []

for _ in range(N):
    i, *num = sys.stdin.readline().split()
    
    if i == 'push':
        result.append(int(*num))

    elif i == 'pop':
        if result:
            print(result.pop())
        else:
            print(-1)

    elif i == 'size':
        print(len(result))

    elif i == 'empty':
        if result:
            print(0)
        else:
            print (1)

    elif i == 'top':
        if result:
            print(result[-1])
        else:
            print(-1)
