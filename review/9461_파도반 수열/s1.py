import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    P = [0, 1, 1, 1]
    for i in range(4, N + 1):
        P.append(P[i - 3] + P[i - 2])
    print(P[N])