import sys
sys.stdin = open('input.txt')

#1 	29200KB	68ms

T = int(input())
for _ in range(T):
    N = int(input())
    temp00 = 1
    temp01 = 0
    temp10 = 0
    temp11 = 1
    n0 = 0
    n1 = 0
    if N == 0:
        n0 = 1
        n1 = 0
    elif N == 1:
        n0 = 0
        n1 = 1
    else:
        for _ in range(2, N + 1):
            n0 = temp00 + temp10
            n1 = temp01 + temp11
            temp00 = temp10
            temp01 = temp11
            temp10 = n0
            temp11 = n1
    print("{} {}".format(n0, n1))


# 2 31864KB	96ms
# from collections import deque
#
# N_list = deque()
# N_list.append((1, 0))
# N_list.append((0, 1))
#
# for i in range(2, 41):
#     N_list.append((N_list[i - 2][0] + N_list[i - 1][0], N_list[i - 2][1] + N_list[i - 1][1]))
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print("{} {}".format(N_list[N][0], N_list[N][1]))