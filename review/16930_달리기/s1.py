import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c, cnt, flag):
    flag2 = 0
    if r == x2 - 1 and c == y2 - 1:
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and N_list[nr][nc] == '.' and not visited[nr][nc]:
            N_list[nr][nc] = '#'
            if r == nr:
                flag2 = 1
                cnt += 1
            elif c == nc:
                flag2 = 2
                cnt += 1
            if (flag and flag2 != flag) or (nr == (x2 - 1) and nc == (y2 - 1)):
                if nr == (x2 - 1) and nc == (y2 - 1):
                    cnt += 1
                result_list[0] += cnt // K + int(bool(cnt % K))
                cnt = 0
            visited[nr][nc] = 1
            dfs(nr, nc, cnt, flag2)
            N_list[nr][nc] = '.'

N, M, K = map(int, input().split())
N_list = [list(input()) for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())
visited = [[0] * M for _ in range(N)]
result_list = [0]
visited[x1 - 1][y1 - 1] = 1
N_list[x1 - 1][y1 - 1] = '#'
dfs(x1 - 1, y1 - 1, -1, 0)
if min(result_list) == 0:
    print(-1)
else:
    print(min(result_list))