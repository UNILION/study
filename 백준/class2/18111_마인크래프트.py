import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
N_list = []
for _ in range(N):
    N_list += map(int, input().split())
time, height = 10e9, 0
len = N * M
for h in range(max(N_list) + 1):
    bottom, top = 0, 0
    for i in range(len):
        if N_list[i] < h:
            bottom += h - N_list[i]
        else:
            top += N_list[i] - h
    if bottom > top + B:
        continue
    t = bottom + top * 2
    if t <= time:
        time = t
        height = h
print(time, height)