# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)

tree = []
while True:
    try:
        num = int(sys.stdin.readline())
        tree.append(num)
    except:
        break

def pre_to_post(tree):    
    def postorder(start, end):
        if start > end:
            return
        div = end + 1
        for i in range(start + 1, end + 1):
            if tree[start] < tree[i]:
                div = i
                break
        postorder(start + 1, div - 1)
        postorder(div, end)
        print(tree[start])
    postorder(0, len(tree) - 1)

pre_to_post(tree)
