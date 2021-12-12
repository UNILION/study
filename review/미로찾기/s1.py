import sys
sys.stdin = open('input.txt')

def dfs(r, c):
    global result           # 결과값 global로 받음
    if N_list[r][c] == 3:   # 도착점인 3을 찾으면
        result = 1          # result를 1로 바꿈
        return              # 함수 탈출

    for i in range(4):      # 네 방향 모두 탐지
        nr = r + dr[i]      # 행
        nc = c + dc[i]      # 열

        # nr과 nc가 0과 N사이이고 nr, nc가 방문하지 않았으면서 해당 미로 좌표가 1이 아니면
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and N_list[nr][nc] != 1:
            visited[nr][nc] = 1 # 방문 체크
            dfs(nr, nc)         # 해당 좌표로 다시 dfs

tc = int(input())   # 총 테스트 케이스 갯수

for t in range(1, tc + 1):
    N = int(input())        # 미로 크기
    result = 0              # 결과값
    N_list = [list(map(int, input())) for _ in range(N)]    # 미로 상태
    visited = [[0] * N for _ in range(N)]                   # 방문 여부

    dr = [-1, 1, 0, 0]  # 행
    dc = [0, 0, -1, 1]  # 열

    for i in range(N):
        for j in range(N):
            if N_list[i][j] == 2:   # 출발점을 찾으면
                dfs(i, j)           # dfs 시작
    

    print("#{} {}".format(t, result))   # 출력