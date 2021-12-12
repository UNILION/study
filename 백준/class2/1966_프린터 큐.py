T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    cnt = 0
    idx = [x for x in range(N)]
    idx[M] = -1
    while True:
        if N_list[0] == max(N_list):
            cnt += 1

            if idx[0] == -1:
                print(cnt)
                break

            else:
                N_list.pop(0)
                idx.pop(0)
        else:
            N_list.append(N_list.pop(0))
            idx.append(idx.pop(0))