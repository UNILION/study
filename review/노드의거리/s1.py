import sys
sys.stdin = open('input.txt')

def bfs(s):
    visited[s] = 0  # 출발 지점 방문 체크
    Q = [s]         # Q에 s를 넣어줌
    while Q:        # Q가 빌 때 까지 반복
        x = Q.pop(0)    # Q의 왼쪽 값을 가져옴
        if x == G:      # x가 도착점이면
            return visited[G]   # 방문값 반환
        for i in range(1, V + 1):
            if not visited[i] and N_list[x][i] == 1:    # 방문하지 않았고 x와 연결된 점이면
                visited[i] = visited[x] + 1 # i의 방문 값은 이전 방문 값 + 1
                Q.append(i) # Q에 i를 넣어줌
    return 0 # 만약에 연결이 안 되어 있으면 0 반환


tc = int(input())

for t in range(1, tc + 1):
    result = 0      # 결과 값
    V, E = map(int, input().split())    # 정점, 간선 정보
    N_list = [[0] * (V + 1) for _ in range(V + 1)]  # 정점 연결 정보
    visited = [0] * (V + 1) # 방문 여부
    for i in range(E):
        sn, en = map(int, input().split())  # 연결 정보
        N_list[sn][en] = 1  # 쌍방향 연결
        N_list[en][sn] = 1  # 쌍방향 연결

    S, G = map(int, input().split())  # 출발, 도착 지점
    result = bfs(S) # 결과값 반환
    print("#{} {}".format(t, result))   # 출력