N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
result = [1] * N
for i in range(N):
    for j in range(N):
        if i != j:
            if N_list[i][0] <= N_list[j][0] and N_list[i][1] <= N_list[j][1]:
                result[i] += 1
print(*result)