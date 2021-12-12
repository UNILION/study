import sys
sys.stdin = open('input.txt')
# 29200KB, 80ms

N = int(input())
N_list = [int(input()) for _ in range(N)]
if N < 3:
    d = [0] * 3
else:
    d = [0] * N

d[0] = N_list[0]
if N >= 2:
    d[1] = N_list[0] + N_list[1]
if N >= 3:
    d[2] = max(N_list[0] + N_list[2], N_list[1] + N_list[2])

for n in range(3, N):
        d[n] = max(d[n - 2] + N_list[n], d[n - 3] + N_list[n - 1] + N_list[n])
print(d[N - 1])