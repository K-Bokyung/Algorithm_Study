# https://www.acmicpc.net/problem/1427

# 1. 입력값 받기
import sys

N = str(sys.stdin.readline().rstrip())

# 2. string으로 바꾼 N의 자릿수를 하나씩 리스트에 append
n_list = []

for i in range(len(N)):
  n_list.append(int(N[i]))

# 3. 다시 숫자로 바꾼 자릿수를 내림차순으로 정렬
n_list.sort(reverse=True)

# 4. 각 자릿수를 다시 string으로 변환
n_list = [str(i) for i in n_list]

# 4. 새로 정렬된 수를 출력
print(''.join(n_list))