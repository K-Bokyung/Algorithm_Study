# https://www.acmicpc.net/problem/9498

# 1
n = int(input())

if 90 <= n <= 100 :
    print('A')
elif 80 <= n <= 89 :
    print('B')
elif 70 <= n <= 79 :
    print('C')
elif 60 <= n <= 69 :
    print('D')
else :
    print('F')

# 2
score = int(input())

if 90 <= score <= 100: print('A')
elif 80 <= score <= 89: print('B')
elif 70 <= score <= 79: print('C')
elif 60 <= score <= 69: print('D')
else: print('F')
