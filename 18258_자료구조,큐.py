# https://www.acmicpc.net/problem/18258

import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for _ in range(N):
    command, *num = sys.stdin.readline().split()
    if command == 'push':
        que.append(int(*num))
    elif command == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(que))
    elif command == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
