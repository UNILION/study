import sys
input = sys.stdin.readline
n = int(input())
n_list = [0] * n
for i in range(n):
    n_list[i] = int(input())
for j in sorted(n_list):
    print(j)