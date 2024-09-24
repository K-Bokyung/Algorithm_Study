# https://www.acmicpc.net/problem/2587

# 1. 입력값 받기
import sys

nums = [int(sys.stdin.readline()) for _ in range(5)]

# 2. 평균 구하기
aver = sum(nums) / 5

# 3. 중앙값 구하기
nums.sort()
mid_num = nums[2]

# 4. 결과값 출력
print(int(aver))
print(mid_num)