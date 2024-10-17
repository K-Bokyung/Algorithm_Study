# https://www.acmicpc.net/problem/2346

import sys
from collections import deque

N = int(sys.stdin.readline())
balloon = deque(enumerate([int(i) for i in sys.stdin.readline().split()]))
result = []

while balloon:
    idx, move = balloon.popleft()
    result.append(idx + 1)
    if move > 0:
        balloon.rotate(-(move - 1))
    elif move < 0:
        balloon.rotate(-move)
        
print(' '.join(map(str, result)))
