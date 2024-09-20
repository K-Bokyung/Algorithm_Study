# https://www.acmicpc.net/problem/15894

# 1. 입력값 받기
import sys

n = int(sys.stdin.readline())

# 2. 밑변의 길이는 n. 위, 오른쪽, 왼쪽 변의 길이를 구하면 된다
# 윗변의 길이는 매 단계에서 0.5 x 2 = 1씩 증가하기 때문에 n
# 오른쪽 변과 왼쪽 변도 각각 n

bottom = n
top = n
side = n

# 3. 결과를 출력

result = n * 4 

print(result)