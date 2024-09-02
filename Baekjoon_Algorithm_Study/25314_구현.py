# https://www.acmicpc.net/problem/25314

# 1. 입력값 받기
import sys

n = int(sys.stdin.readline())

# 2. n이 4의 몇배수인지 알아내기

m = n // 4

# 3. 'int' 앞에 'long'을 m번 붙여서 출력 (띄어쓰기 포함)

print('long '*m + 'int')