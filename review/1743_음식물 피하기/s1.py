import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6) # 	런타임 에러 (RecursionError)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and N_list[nr][nc] == 1 and not visited[nr][nc]:
            N_list[nr][nc] = 0
            visited[nr][nc] = 1
            result_list[-1] += 1
            dfs(nr, nc)

N, M, K = map(int, input().split())
N_list = [[0] * M for _ in range(N)]
for k in range(K):
    x, y = map(int, input().split())
    N_list[x - 1][y - 1] = 1
visited = [[0] * M for _ in range(N)]
result_list = []
for i in range(N):
    for j in range(M):
        if N_list[i][j] == 1:
            visited[i][j] = 1
            N_list[i][j] = 0
            result_list.append(1)
            dfs(i, j)
print(max(result_list))