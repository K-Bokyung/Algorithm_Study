# https://www.acmicpc.net/problem/18870

# 1. 입력값 받기
import sys
from collections import defaultdict

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

# 2. Xi > Xj를 만족하는 개수를 리스트로 저장
X_list = sorted(set(X))
X_dict = {X_list[i] : i for i in range(len(X_list))}

# 3. 결과 출력
for i in X:
  print(X_dict[i], end = ' ')