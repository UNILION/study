import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
dr = [-1, 1, 0, 0]  # 상하
dc = [0, 0, -1, 1]  # 좌우

def dfs_w(r, c):
    global W_C  # W의 인원 변수 W_C를 글로벌로 받아옴
    if not visited[r][c]:   # r, c 좌표가 아직 방문 안 했다면
        visited[r][c] = 1   # 방문 처리 후
        W_C += 1            # W_C + 1
    for k in range(4):      # 네 방향 탐색
        nr = r + dr[k]
        nc = c + dc[k]
        # 새로운 좌표의 행이 0과 M사이이고 열이 0과 N 사이이면서 해당 좌표가 방문하지 않았고 값이 W이면
        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and N_list[nr][nc] == 'W':
            dfs_w(nr, nc)   # 해당 좌표 값으로 dfs_w 함수를 돈다.
    return W_C ** 2 # W_C의 제곱 값을 반환


def dfs_b(r, c):
    global B_C  # W의 인원 변수 B_C를 글로벌로 받아옴
    if not visited[r][c]:   # r, c 좌표가 아직 방문 안 했다면
        visited[r][c] = 1   # 방문 처리 후
        B_C += 1            # B_C + 1
    for k in range(4):      # 네 방향 탐색
        nr = r + dr[k]
        nc = c + dc[k]
        # 새로운 좌표의 행이 0과 M사이이고 열이 0과 N 사이이면서 해당 좌표가 방문하지 않았고 값이 B이면
        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and N_list[nr][nc] == 'B':
            dfs_b(nr, nc)   # 해당 좌표 값으로 dfs_b 함수를 돈다.
    return B_C ** 2 # B_C의 제곱 값을 반환


N, M = map(int, input().split())    # 가로, 세로 크기
N_list = [list(map(str, input())) for _ in range(M)]    # 병사 정보
W = B = 0       # 결과값

visited = [[0] * N for _ in range(M)]   # 방문 여부
for i in range(M):      # 행은 세로이므로 M
    for j in range(N):  # 열은 가로이므로 N
        if not visited[i][j]:   # i, j 좌표를 방문하지 않았다면
            W_C = B_C = 0  # 연속된 아군, 적군 인원
            if N_list[i][j] == 'W': # 현재 좌표 값이 W라면
                W += dfs_w(i, j)    # i,j를 dfs_w 돌려서 나온 값을 W에 더한다.
            elif N_list[i][j] == 'B': # 현재 좌표 값이 B라면
                B += dfs_b(i, j)    # i,j를 dfs_b 돌려서 나온 값을 B에 더한다.
print(W, B) # W, B 출력