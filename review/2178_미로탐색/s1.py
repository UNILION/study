import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global result
    stack = deque()
    stack.append((r, c))
    N_list[0][0] = 1
    while stack:
        x, y = stack.popleft()
        if x == N - 1 and y == M - 1:
            print(N_list[x][y])

        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0 <= nr < N and 0 <= nc < M and N_list[nr][nc] == '1':
                stack.append((nr, nc))
                N_list[nr][nc] = N_list[x][y] + 1

def dfs(r, c, cnt):
    global result
    if result < cnt:
        return

    if r == N - 1 and c == M - 1:
        if result > cnt:
            result = cnt
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and N_list[nr][nc] == '1':
            N_list[nr][nc] = '0'
            dfs(nr, nc, cnt + 1)
            N_list[nr][nc] = '1'

N, M = map(int, input().split())
N_list = [list(input()) for _ in range(N)]
result = N*M
# dfs(0, 0, 1)
bfs(0, 0)