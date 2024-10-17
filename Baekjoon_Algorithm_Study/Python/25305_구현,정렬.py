# https://www.acmicpc.net/problem/25305

# 1. 입력값 받기
import sys

N, k = list(map(int, sys.stdin.readline().split()))
scores = list(map(int, sys.stdin.readline().split()))

# 2. 점수를 내림차순으로 정렬
scores.sort(reverse=True)

# 3. 상을 받는 마지막 사람의 점수를 index로 찾기
cut_line = scores[k-1]

print(cut_line)