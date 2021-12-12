import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * N for _ in range(N)]
idx = 2
d[0][0] = N_list[0][0]
for i in range(1, N):
    for j in range(idx):
        if j == 0:
            d[i][j] = d[i - 1][j] + N_list[i][j]
        elif j == idx - 1:
            d[i][j] = d[i - 1][j - 1] + N_list[i][j]
        else:
            d[i][j] = max(d[i - 1][j - 1] + N_list[i][j], d[i - 1][j] + N_list[i][j])
    idx += 1
print(max(d[N - 1]))