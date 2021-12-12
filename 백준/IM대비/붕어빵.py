tc = int(input())

for t in range(1, tc + 1):
    flag = 0
    N, M, K = map(int, input().split())
    custom = list(map(int, input().split()))
    custom.sort()
    
    for j in range(1, N//K + 2):
        if custom[0] < M:
            result = "Impossible"

        cnt = 0
        boong = K *(j-1)
        for i in range(N):
            if custom[i] < M * j:   # 초가 j 사이클 보다 적은 인원 수
                cnt += 1
                custom.pop(0)

        if cnt > boong:       # 붕어빵 갯수보다 많으면
            result = "Impossible"
            flag = 1
            break
        boong -= cnt
    if flag == 0:
        result = "Possible"

    print("#{} {}".format(t, result))