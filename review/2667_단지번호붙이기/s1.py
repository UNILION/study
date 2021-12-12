import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N and N_list[nr][nc] == '1':
            N_list[nr][nc] = '0'
            result_list[-1] += 1
            print(result_list)
            dfs(nr, nc)

N = int(input())
N_list = [list(str(input())) for _ in range(N)]
result_list = []
for i in range(N):
    for j in range(N):
        if N_list[i][j] == '1':
            N_list[i][j] = '0'
            result_list.append(1)
            dfs(i, j)
result_list.sort()
print(len(result_list))
for result in result_list:
    print(result)