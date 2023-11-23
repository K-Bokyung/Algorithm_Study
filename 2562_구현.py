# https://www.acmicpc.net/problem/2562

# 1
num_list = []

for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list)) + 1)

# 2
num_list = []
max_num = 0
max_index = 0

for i in range(9):
    num = int(input())
    num_list.append(num)

for i in range(9):
    if num_list[i] > max_num:
        max_num = num_list[i]
        max_index = i + 1

print(max_num)
print(max_index)
