import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
if len(N_list) == 1:
    print(N_list[0] - M)
else:
    N_list = sorted(N_list, reverse=True)
    idx = 0
    result = 0
    while True:
        result += (N_list[idx] - N_list[idx + 1]) * (idx + 1)
        if result < M:
            idx += 1
            if idx == len(N_list) - 1:
                temp = N_list[idx]
                temp += (result - M) // (idx + 1)
                print(temp)
                break
            continue
        else:
            if result == M:
                print(N_list[idx + 1])
                break
            elif result > M:
                temp = N_list[idx + 1]
                temp += (result - M) // (idx + 1)
                print(temp)
                break