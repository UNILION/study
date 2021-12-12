import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N + 1):
    flag = 1
    if i == 1:
        continue
    if i == 2 or i == 3:
        print(i)
        continue
    if i % 2 == 0:
        continue

    for j in range(3, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = 0
            break
    if flag:
        print(i)