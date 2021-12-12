import sys
input = sys.stdin.readline

N = int(input())
check = [0 for x in range(-4000, 4001)]

count = 1
count_list = []
for _ in range(N):
    x = int(input())
    check[x] += 1
    if check[x] == count:
        count_list.append(x)
    if check[x] > count:
        count_list = []
        count_list.append(x)
        count = check[x]

if N == 1:
    print(x)
    print(x)
    print(x)
    print(0)
else:
    # 산술
    check_a = 0
    check_b = N//2 + 1
    check_c = 0
    temp_a = 0
    flag_b = 1
    flag_d = 1
    max_x = 0
    min_x = 0

    if len(count_list) == 1:
        check_c = count_list[0]
    else:
        for j in range(2):
            for k in range(j + 1, len(count_list)):
                if count_list[j] > count_list[k]:
                    count_list[j], count_list[k] = count_list[k], count_list[j]
        check_c = count_list[1]

    for a in range(-4000, 4002):
        if check_a == N:
            max_x = a - 1
            break
        if check[a] != 0:
            if flag_d:
                flag_d = 0
                min_x = a

            check_a += check[a]
            temp_a += a * check[a]
            if flag_b and check_b <= check_a:
                check_b = a
                flag_b = 0

    if temp_a % N >= N / 2:
        print(temp_a // N + 1)
    else:
        print(temp_a // N)
    # 중앙
    print(check_b)
    # 최빈
    print(check_c)
    # 범위
    print(max_x - min_x)