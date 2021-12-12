import sys
sys.stdin = open('input.txt')

def nogada(n, cnt):
    if n > N:
        return
    if d[n] > cnt:
        d[n] = cnt
        if n == N:
            return
        if n + 5 <= N:
            nogada(n + 5, cnt + 1)
        if n + 3 <= N:
            nogada(n + 3, cnt + 1)

N = int(input())
cnt = 0
d = [1e9] * (N + 1)
nogada(0, cnt)
if d[N] == 1e9:
    d[N] = -1
print(d[N])