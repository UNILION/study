tc = int(input())

for t in range(1, tc + 1):
    N = int(input())
    n_list = list(map(int, input().split()))
    multi = 0
    result = -1

    for n in range(N - 1):
        for m in range(n + 1, N):
            multi = n_list[n] * n_list[m]
            str_multi = str(multi)
            flag = 0
            
            for i in range(len(str_multi) - 1):
                if int(str_multi[i]) <= int(str_multi[i + 1]):
                    flag = 1
                else:
                    flag = 0
                    break
            
            if len(str_multi) == 1:
                flag = 1
                
            if flag == 1:
                if result < multi:
                    result = multi

    if N == 1:
        result = n_list[0]
    print("#{} {}".format(t, result))

"""
3
6
5 4 7 4 3 6
4
3 148 2 1
10
9 5 9 4 9 3 9 2 9 1
"""