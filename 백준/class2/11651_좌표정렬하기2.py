import sys
input = sys.stdin.readline

"""
57672KB, 384ms => import sys O
57672KB, 4428ms => import sys X
"""

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
N_list = sorted(N_list, key = lambda x:(x[1], x[0]))
for n in N_list:
    print(*n)