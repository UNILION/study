import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(x):
    stack = set()   # deque도 시간 초과...!
    stack.add(x)

    while stack:
        y = stack.pop()
        if not visited[y]:
            visited[y] = 1
            for z in N_list[y]:
                stack.add(z)

N, M = map(int, input().split())
N_list = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    N_list[u].append(v)
    N_list[v].append(u)

result = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        result += 1
print(result)