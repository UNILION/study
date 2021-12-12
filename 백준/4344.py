for _ in range(int(input())):
    N_list = list(map(int, input().split()))
    plus = sum(N_list[1:])
    aver = plus / N_list[0]
    res = 0
    for i in range(1, N_list[0] + 1):
        if N_list[i] > aver:
            res += 1
    print("{:.3f}%".format(res / N_list[0] * 100))