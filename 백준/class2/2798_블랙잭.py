N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort(reverse=True)
temp = 0
result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            temp = N_list[i] + N_list[j] + N_list[k]
            if temp <= M:
                if temp > result:
                    result = temp
print(result)