# https://www.acmicpc.net/problem/1541

import sys

nums = list(map(str, sys.stdin.readline().strip().split('-')))

min_result = 0

for i in nums[0:1]:
    for j in i.split('+'):
        min_result += int(j)

for i in nums[1:]:
    for j in i.split('+'):
        min_result -= int(j)

print(min_result)
