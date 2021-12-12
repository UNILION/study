import sys
from itertools import product
N, M = map(int, input().split())
N_list = [0] * N
for i in range(N):
    N_list[i] = i + 1
N_list = list(product(N_list, repeat=M))
for n in N_list:
    for m in n:
        print(m,end=" ")
    print()