import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]  # 상하
dc = [0, 0, -1, 1]  # 좌우

def dfs(r, c):
    global result           # 결과값 global로 받아옴
    visited[r][c] = 1       # visited 체크
    if N_list[r][c] == 3:   # 도착점이면
        result = 1          # result 1 표시
        return              # 함수 탈출

    for k in range(4):      # 네 방향 탐지
        nr = r + dr[k]      # nr 정의
        nc = c + dc[k]      # nc 정의
        # nr, nc가 0과 16 사이이고 방문하지 않고 1이 아니면
        if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and N_list[nr][nc] != 1:
            dfs(nr, nc) # 다음 좌표를 dfs

for t in range(1, 11):
    tc = int(input())
    result = 0      # 결과 값
    flag = 0        # 반복문 빠져나가기 위한 것

    N_list = [list(map(int, input())) for _ in range(16)]   # 미로 정보

    visited = [[0] * 16 for _ in range(16)] # 방문 여부

    for i in range(16):
        for j in range(16):
            if N_list[i][j] == 2:   # 출발점 발견
                dfs(i, j)           # dfs 함수
                flag = 1            # flag = 1
                break               # 탈출
        if flag == 1:               # flag가 1이면
            break                   # 탈출

    print("#{} {}".format(t, result))       # 출력