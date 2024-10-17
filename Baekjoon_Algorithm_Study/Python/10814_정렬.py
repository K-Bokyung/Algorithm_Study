# https://www.acmicpc.net/problem/10814

import sys

N = int(sys.stdin.readline())
saram = [sys.stdin.readline().split() for _ in range(N)]

saram.sort(key=lambda x:int(x[0]))

for i in saram:
    print(*i)
