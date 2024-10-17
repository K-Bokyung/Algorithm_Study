# https://www.acmicpc.net/problem/10813

n, m = [int(i) for i in input().split()]
n_list = [i for i in range(n + 1)]
b_change = [input().split() for _ in range(m)]

for i in range(m):
    n_list[int(b_change[i][0])], n_list[int(b_change[i][1])] = n_list[int(b_change[i][1])], n_list[int(b_change[i][0])]

print(*n_list[1:])
