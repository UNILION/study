import sys
input = sys.stdin.readline

tc = int(input())
coloring = [[0] * 100 for _ in range(100)]

for _ in range(tc):
    r, c = map(int, input().split())
    for i in range(10):
        for j in range(10):
            coloring[r + i][c + j] = 1  # 색종이 있는 곳은 1로 채움

cnt = 0
for i in range(100):
    for j in range(100):
        if coloring[i][j] == 1:
            cnt += 1                    # 해당 자리가 1이면 cnt + 1

print(cnt)