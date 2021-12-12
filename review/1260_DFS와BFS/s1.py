import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = [v]     # v를 스택에 넣어줌
    while stack:    # stack이 빌 때 까지 반복
        x = stack.pop()     # stack에 있는 것을 pop
        if not visited[x]:  # x가 방문하지 않았다면
            print(x, end=" ")   # 출력
            visited[x] = 1      # x 방문 표시
            for i in range(N, 0, -1):   # 숫자 작은 순대로 해야 하므로 거꾸로 탐색
                if N_list[x][i] == 1 and not visited[i]:    # 서로 연결되어 있고 방문하지 않았다면
                    stack.append(i) # stack에 추가
    return print()  # bfs 출력도 해야 하므로 띄기

def bfs(v):
    stack = [v]     # v를 스택에 넣어줌
    while stack:    # stack이 빌 때까지 반복
        x = stack.pop(0)    # 너비우선 탐색이므로 먼저 쌓인 것을 빼줌
        if not visited[x]:  # x가 방문하지 않았다면
            print(x, end=" ")   # 출력
            visited[x] = 1      # x 방문 표시
            for i in range(1, N + 1):   # 전체 탐색
                if N_list[x][i] == 1 and not visited[i]:    # 서로 연결되어 있고 방문하지 않았다면
                    stack.append(i) # stack에 추가
    return print()  # 그 다음 출력 있을 수 있으므로

N, M, V = map(int, input().split())     # 정점, 간선, 시작점
N_list = [[0] * (N + 1) for _ in range(N + 1)]  # 연결 정보 담기
visited = [0] * (N + 1)     # 방문 표시

for i in range(M):
    s, e = map(int, input().split())    # 쌍방향 연결 좌표
    N_list[s][e] = 1    # 인접 행렬
    N_list[e][s] = 1    # 인접 행렬

dfs(V)  # dfs 함수
visited = [0] * (N + 1) # visited 초기화
bfs(V)  # bfs 함수