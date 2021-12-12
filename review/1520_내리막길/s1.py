import sys
# sys.stdin = open('input.txt')
# https://velog.io/@nnnyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%92%80%EC%9D%B4-%EB%B6%84%EC%84%9D-BOJ-1520-%EB%82%B4%EB%A6%AC%EB%A7%89%EA%B8%B8-DFS-%EB%A1%9C-%ED%92%80%EA%B8%B0
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    if r == N - 1 and c == M - 1:
        dp[r][c] = 1
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and N_list[r][c] > N_list[nr][nc]:
            dp[r][c] += dfs(nr, nc)

    return dp[r][c] # 이거 안 하면 None 반환

N, M = map(int, input().split())
N_list = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dfs(0, 0)
print(dp[0][0])