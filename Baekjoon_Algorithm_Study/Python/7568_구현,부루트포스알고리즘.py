# https://www.acmicpc.net/problem/7568

import sys

N = int(sys.stdin.readline())
member = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
result = []

for i in range(N):
    count = 0
    for j in range(N):
        # i가 j보다 덩치가 작을 때만 count가 증가. 그 외는 다음 i, j로 넘어감.
        if member[i][0] < member[j][0] and member[i][1] < member[j][1]:
            count += 1
    result.append(count + 1)

print(*result)