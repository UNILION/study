import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = [v]     # stack에 v를 넣음
    result = -1     # 처음 값은 제외해야 하므로 -1로 초기화
    while stack:    # stack이 빌 때 까지 반복
        x = stack.pop()     # stack 마지막 값을 꺼내줌
        if not visited[x]:  # x가 방문하지 않았다면
            visited[x] = 1  # 방문 표시
            result += 1     # 결과 + 1
            for i in range(N + 1):  # 전체 탐색
                if N_list[x][i] == 1 and not visited[i]:    # 서로 연결 되어 있고 방문 하지 않았다면
                    stack.append(i)     # stack에 i를 추가
    print(result)   # 결과 출력

N = int(input())    # 컴퓨터 총 수
M = int(input())    # 연결 정보
N_list = [[0] * (N + 1) for _ in range(N + 1)]  # 연결 정보 담을 인접 행렬
for _ in range(M):
    s, e = map(int, input().split())    # 쌍방향 정보
    N_list[s][e] = 1        # 쌍방향 연결 1
    N_list[e][s] = 1        # 쌍방향 연결 1
visited = [0] * (N + 1)     # visited 를 N + 1개 만큼 만들어줌
dfs(1)  # 시작점 1로 DFS