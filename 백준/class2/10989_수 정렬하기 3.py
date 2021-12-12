import sys
input = sys.stdin.readline

N = int(input())
check = [0] * 10001
for _ in range(N):
    x = int(input())
    check[x] += 1

for i in range(10001):
    if check[i] != 0:
        for _ in range(check[i]):
            print(i)